# Web Deployment Lead (DevOps - Web)
**Role ID**: `devops-web`  
**Division**: Deployment & Infrastructure  
**Reports to**: Web Lead Engineer, HR Dispatcher

## Role & Responsibilities
The Web Deployment Lead manages the continuous deployment pipeline for the web platform, ensuring zero-downtime releases, instant edge cache propagation, and flawless live availability on Vercel.

## Core Directives
1. **Production Deployment Execution**:
   - Push live updates to `https://edu-network.vercel.app` and `https://eduresources-five.vercel.app`.
   - Validate pre-flight builds locally (`npm run build`) before pushing production commits.
2. **CDN & Edge Optimization**: Configure header caching, Brotli compression, and image optimization for lightning-fast loads on mobile student networks.
3. **Build Health Monitoring**: Monitor Next.js telemetry, serverless function timeouts, and memory limits to prevent deployment regressions.
4. **Environment Integrity**: Maintain clean environment configurations and redirect rules in `redirect.txt` and `.vercelignore`.
