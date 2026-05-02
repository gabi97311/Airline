"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth-context";
import toast from "react-hot-toast";
import { Plane } from "lucide-react";

export default function AuthPage() {
  const { login, register, isLoggedIn } = useAuth();
  const router = useRouter();
  const [mode, setMode] = useState<"login" | "register">("login");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  if (isLoggedIn) {
    router.push("/");
    return null;
  }

  const handleSubmit = async () => {
    if (!username || !password) {
      toast.error("Заполните все поля");
      return;
    }
    setLoading(true);
    try {
      if (mode === "login") {
        await login(username, password);
        toast.success("Добро пожаловать!");
      } else {
        await register(username, password);
        toast.success("Аккаунт создан!");
      }
      router.push("/");
    } catch (err: any) {
      toast.error(err?.response?.data?.detail ?? "Ошибка. Проверьте данные.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-[calc(100vh-56px)] bg-sky-cream flex items-center justify-center px-4">
      <div className="w-full max-w-sm">
        {/* Logo */}
        <div className="flex items-center justify-center gap-2 mb-8">
          <div className="w-8 h-8 rounded-xl bg-navy flex items-center justify-center">
            <Plane className="w-4 h-4 text-sky-gold" />
          </div>
          <span className="font-serif text-2xl text-navy">SkyBook</span>
        </div>

        <div className="bg-white border border-gray-200 rounded-2xl p-8 shadow-sm">
          <h1 className="font-serif text-2xl mb-1">
            {mode === "login" ? "Добро пожаловать" : "Создать аккаунт"}
          </h1>
          <p className="text-sm text-gray-400 mb-7">
            {mode === "login"
              ? "Войдите, чтобы бронировать билеты"
              : "Зарегистрируйтесь для бронирования"}
          </p>

          <div className="space-y-4">
            <div>
              <label className="block text-xs text-gray-400 uppercase tracking-wider mb-1.5 font-medium">
                Имя пользователя
              </label>
              <input
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="username"
                autoComplete="username"
                className="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-sm outline-none focus:border-sky-blue transition-colors"
                onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
              />
            </div>
            <div>
              <label className="block text-xs text-gray-400 uppercase tracking-wider mb-1.5 font-medium">
                Пароль
              </label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                autoComplete="current-password"
                className="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-sm outline-none focus:border-sky-blue transition-colors"
                onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
              />
            </div>
          </div>

          <button
            onClick={handleSubmit}
            disabled={loading}
            className="w-full mt-6 bg-navy text-white py-3 rounded-xl text-sm font-medium hover:bg-sky-blue transition-colors disabled:opacity-50"
          >
            {loading
              ? "..."
              : mode === "login"
              ? "Войти в аккаунт"
              : "Зарегистрироваться"}
          </button>

          <div className="flex items-center gap-3 my-5">
            <div className="flex-1 h-px bg-gray-100" />
            <span className="text-xs text-gray-300">или</span>
            <div className="flex-1 h-px bg-gray-100" />
          </div>

          <p className="text-sm text-center text-gray-400">
            {mode === "login" ? "Нет аккаунта?" : "Уже есть аккаунт?"}{" "}
            <button
              onClick={() => setMode(mode === "login" ? "register" : "login")}
              className="text-sky-blue hover:underline"
            >
              {mode === "login" ? "Зарегистрироваться" : "Войти"}
            </button>
          </p>
        </div>
      </div>
    </div>
  );
}
