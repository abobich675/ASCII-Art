// import type { NextConfig } from "next";

const nextConfig = {
  output: "standalone",
  experimental: {
    serverActions: {
      bodySizeLimit: '5mb' // or larger depending on your needs
    }
  },
  allowedHosts: [
    'jared.bobich.us',
    'bobich.us'
  ],
};

export default nextConfig;
