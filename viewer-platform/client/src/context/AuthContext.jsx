import React, { createContext, useContext, useState, useEffect } from 'react';
import { api } from '../services/api';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [googleClientId, setGoogleClientId] = useState('');
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);

  useEffect(() => {
    async function init() {
      try {
        const config = await api.getAuthConfig();
        if (config.googleClientId) {
          setGoogleClientId(config.googleClientId);
        }

        const currentUser = await api.getCurrentUser();
        if (currentUser) {
          setUser(currentUser);
        }
      } catch (err) {
        console.error('Auth initialization error:', err);
      } finally {
        setLoading(false);
      }
    }
    init();
  }, []);

  const loginWithGoogleCredential = async (credential) => {
    const data = await api.loginWithGoogle(credential);
    setUser(data.user);
    setIsLoginModalOpen(false);
    return data.user;
  };

  const loginWithDemo = async (name, email) => {
    const data = await api.loginDemo(name, email);
    setUser(data.user);
    setIsLoginModalOpen(false);
    return data.user;
  };

  const logout = async () => {
    await api.logout();
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        googleClientId,
        isLoginModalOpen,
        setIsLoginModalOpen,
        loginWithGoogleCredential,
        loginWithDemo,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}
