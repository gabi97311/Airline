import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'standalone', 
  async rewrites() {
    return [
      {
        source: "/api/auth/:path*",
        // Берем URL из Docker Compose, либо дефолт для локалки
        destination: `${process.env.AUTH_SERVICE_URL || 'http://localhost:8001'}/:path*`,
      },
      {
        source: "/api/payment/:path*",
        destination: `${process.env.BACKEND_SERVICE_URL || 'http://localhost:8000'}/payment/:path*`,
      },
      {
        source: "/api/:path*",
        destination: `${process.env.BACKEND_SERVICE_URL || 'http://localhost:8000'}/:path*`,
      },
    ];
  },
};

export default nextConfig;