import { describe, it, expect } from 'vitest';
import { loadConfig } from '../lib/config.mjs';

describe('loadConfig', () => {
  it('loads course.config.json from project root', () => {
    const cfg = loadConfig();
    expect(cfg.course).toBe('tartak');
    expect(cfg.languages).toEqual(['pl', 'en', 'es', 'uk']);
    expect(cfg.modules).toHaveLength(3);
  });

  it('has default language ES', () => {
    const cfg = loadConfig();
    expect(cfg.defaultLanguage).toBe('es');
  });
});
