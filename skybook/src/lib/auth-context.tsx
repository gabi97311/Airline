"use client";

import React, { createContext, useContext, useState, useEffect, ReactNode } from "react";
import { authService } from "@/lib/api";

interface AuthState {
  user: { id: number; user_name: string; role: string } | null;
  isLoading: boolean;
  isLoggedIn: boolean;
  login: (username: string, password: string) => Promise<void>;
  register: (username: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthState | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<AuthState["user"]>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    authService.me()
      .then(setUser)
      .catch(() => setUser(null))
      .finally(() => setIsLoading(false));
  }, []);

  const login = async (username: string, password: string) => {
    await authService.login({ username, password });
    const me = await authService.me();
    setUser(me);
  };

  const register = async (username: string, password: string) => {
    await authService.register({ user_name: username, user_password: password });
    await login(username, password);
  };

  const logout = () => {
    document.cookie = "access_token=; Max-Age=0";
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, isLoading, isLoggedIn: !!user, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx;
}
