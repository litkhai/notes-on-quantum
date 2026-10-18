import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { createServer } from "node:net";
import { after, before, test } from "node:test";
import { fileURLToPath } from "node:url";

// Runs against the production build (`npm run build` first) served by `next start`.
const appDir = fileURLToPath(new URL("..", import.meta.url));
let server;
let base;

function freePort() {
  return new Promise((resolve, reject) => {
    const probe = createServer();
    probe.once("error", reject);
    probe.listen(0, "127.0.0.1", () => {
      const { port } = probe.address();
      probe.close(() => resolve(port));
    });
  });
}

before(async () => {
  const port = await freePort();
  base = `http://127.0.0.1:${port}`;
  // Sample mode: no ClickHouse credentials reach the test server.
  const env = { ...process.env, CLICKHOUSE_DEMO_MODE: "sample", CLICKHOUSE_HOST: "", CLICKHOUSE_PASSWORD: "" };
  server = spawn("npx", ["next", "start", "-p", String(port), "-H", "127.0.0.1"], { cwd: appDir, env, stdio: "ignore" });
  for (let attempt = 0; attempt < 60; attempt += 1) {
    try {
      if ((await fetch(`${base}/api/health`)).ok) return;
    } catch {
      // server not listening yet
    }
    await new Promise((resolve) => setTimeout(resolve, 250));
  }
  throw new Error("next start did not become healthy");
});

after(() => {
  server?.kill();
});

test("renders the Korean quantum observability lab", async () => {
  const response = await fetch(`${base}/`, { headers: { accept: "text/html" } });
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /<html[^>]+lang="ko"/i);
  assert.match(html, /<title>Quantum Shot Observatory<\/title>/i);
  assert.match(html, /한 번의 측정은 우연이지만/);
  assert.match(html, /반복하면 변화가 보입니다/);
  assert.doesNotMatch(html, /codex-preview|react-loading-skeleton/i);
});

test("serves every query preset in sample mode without credentials", async () => {
  const presets = [
    "summary", "distribution", "drift", "errors", "experiments",
    "degradation", "entropy",
  ];
  for (const preset of presets) {
    const response = await fetch(`${base}/api/query?preset=${preset}&experiment=latest`);
    assert.equal(response.status, 200, preset);
    const payload = await response.json();
    assert.equal(payload.source, "sample", preset);
    assert.equal(payload.preset.id, preset);
    assert.ok(payload.data.length > 0, preset);
  }
});

test("rejects an invalid experiment id", async () => {
  const response = await fetch(`${base}/api/query?preset=distribution&experiment=not-a-uuid`);
  assert.equal(response.status, 400);
});

test("exposes a Docker health endpoint", async () => {
  const response = await fetch(`${base}/api/health`);
  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), {
    status: "ok",
    service: "quantum-shot-observatory",
  });
});
