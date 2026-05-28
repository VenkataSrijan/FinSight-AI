import type { NextConfig } from "next";
import path from "node:path";

const nextConfig: NextConfig = {
  turbopack: {
    root: path.resolve(__dirname, "../.."),
  },

  experimental: {
    optimizePackageImports: [
      "lucide-react",
      "@tanstack/react-query",
    ],
  },

  images: {
    remotePatterns: [],
  },

  poweredByHeader: false,

  reactStrictMode: true,
};

export default nextConfig;