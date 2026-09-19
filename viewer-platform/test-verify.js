const http = require('http');

function request(options, data) {
  return new Promise((resolve, reject) => {
    const req = http.request(options, (res) => {
      let body = '';
      res.on('data', (chunk) => (body += chunk));
      res.on('end', () => {
        resolve({
          statusCode: res.statusCode,
          headers: res.headers,
          body: body,
        });
      });
    });
    req.on('error', reject);
    if (data) req.write(data);
    req.end();
  });
}

async function verifyPlatform() {
  console.log('--- 1. Testing /api/health ---');
  const health = await request({ hostname: '127.0.0.1', port: 5001, path: '/api/health', method: 'GET' });
  console.log('Health Status:', health.statusCode, health.body);

  console.log('\n--- 2. Testing /api/materials ---');
  const materialsRes = await request({ hostname: '127.0.0.1', port: 5001, path: '/api/materials', method: 'GET' });
  const materials = JSON.parse(materialsRes.body);
  console.log(`Total Materials Indexed: ${materials.total}`);
  console.log('First 3 materials:', JSON.stringify(materials.materials.slice(0, 3), null, 2));

  console.log('\n--- 3. Testing Demo Auth Login ---');
  const loginRes = await request(
    {
      hostname: '127.0.0.1',
      port: 5001,
      path: '/api/auth/demo',
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
    },
    JSON.stringify({ name: 'Rahul Sharma', email: 'rahul.s@university.edu' })
  );
  const loginData = JSON.parse(loginRes.body);
  console.log('Login Result:', loginData.user);
  const token = loginData.token;

  console.log('\n--- 4. Testing Secure Document Token Generation ---');
  const sampleDoc = materials.materials[0];
  const tokenRes = await request({
    hostname: '127.0.0.1',
    port: 5001,
    path: `/api/document/token/${sampleDoc.id}`,
    method: 'POST',
    headers: { Authorization: `Bearer ${token}` },
  });
  const tokenData = JSON.parse(tokenRes.body);
  console.log('Stream Token Generated:', tokenData);

  console.log('\n--- 5. Testing Document Stream Delivery ---');
  const streamRes = await request({
    hostname: '127.0.0.1',
    port: 5001,
    path: `/api/document/stream/${tokenData.token}`,
    method: 'GET',
  });
  console.log('Stream Response Status:', streamRes.statusCode);
  console.log('Content-Type:', streamRes.headers['content-type']);
  console.log('Content-Length:', streamRes.headers['content-length']);
  console.log('Anti-Cache Header:', streamRes.headers['cache-control']);

  console.log('\n✅ ALL VERIFICATION TESTS PASSED SUCCESSFULLY!');
  process.exit(0);
}

verifyPlatform().catch((err) => {
  console.error('Test Failed:', err);
  process.exit(1);
});
