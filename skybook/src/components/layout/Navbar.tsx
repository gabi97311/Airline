"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Plane, Ticket, Settings, LogOut, User } from "lucide-react";
import { useAuth } from "@/lib/auth-context";
import clsx from "clsx";

const navLinks = [
  { href: "/", label: "Поиск" },
  { href: "/tickets", label: "Мои билеты" },
];

const adminLinks = [
  { href: "/admin/flights", label: "Рейсы" },
  { href: "/admin/airplanes", label: "Самолёты" },
];

export function Navbar() {
  const pathname = usePathname();
  const { user, isLoggedIn, logout } = useAuth();

  return (
    <header className="bg-navy sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-6 h-14 flex items-center justify-between">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-2 group">
          <div className="w-7 h-7 rounded-lg bg-sky-gold/20 flex items-center justify-center group-hover:bg-sky-gold/30 transition-colors">
            <Plane className="w-4 h-4 text-sky-gold" />
          </div>
          <span className="font-serif text-xl text-white tracking-tight">SkyBook</span>
        </Link>

        {/* Nav links */}
        <nav className="hidden md:flex items-center gap-1">
          {navLinks.map(({ href, label }) => (
            <Link
              key={href}
              href={href}
              className={clsx(
                "px-3 py-1.5 rounded-lg text-sm transition-colors",
                pathname === href
                  ? "bg-white/10 text-white"
                  : "text-white/50 hover:text-white hover:bg-white/5"
              )}
            >
              {label}
            </Link>
          ))}
          {user?.role === "admin" &&
            adminLinks.map(({ href, label }) => (
              <Link
                key={href}
                href={href}
                className={clsx(
                  "px-3 py-1.5 rounded-lg text-sm transition-colors",
                  pathname.startsWith(href)
                    ? "bg-sky-gold/20 text-sky-gold"
                    : "text-white/50 hover:text-sky-gold/80 hover:bg-sky-gold/10"
                )}
              >
                {label}
              </Link>
            ))}
        </nav>

        {/* Auth section */}
        <div className="flex items-center gap-2">
          {isLoggedIn ? (
            <>
              <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-white/5">
                <User className="w-3.5 h-3.5 text-white/60" />
                <span className="text-sm text-white/80">{user?.user_name}</span>
              </div>
              <button
                onClick={logout}
                className="p-1.5 rounded-lg text-white/40 hover:text-white hover:bg-white/10 transition-colors"
                title="Выйти"
              >
                <LogOut className="w-4 h-4" />
              </button>
            </>
          ) : (
            <Link
              href="/auth"
              className="px-4 py-1.5 bg-sky-blue text-white text-sm rounded-lg hover:bg-blue-600 transition-colors font-medium"
            >
              Войти
            </Link>
          )}
        </div>
      </div>
    </header>
  );
}
