import { readFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '../..');

export function loadConfig(configPath = 'course.config.json') {
  const path = resolve(PROJECT_ROOT, configPath);
  return JSON.parse(readFileSync(path, 'utf8'));
}
