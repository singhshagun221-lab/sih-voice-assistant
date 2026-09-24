import { startTunnel } from 'untun';

process.env.UNTUN_ACCEPT_CLOUDFLARE_NOTICE = '1';

async function main() {
  console.log('Provisioning Cloudflare trycloudflare tunnel for port 8000...');
  const tunnel = await startTunnel({
    port: 8000,
    acceptCloudflareNotice: true
  });
  const url = await tunnel.getURL();
  console.log('CLOUDFLARE_TUNNEL_URL=' + url);
}

main().catch(err => {
  console.error('Error starting Cloudflare tunnel:', err);
});
