import { describe, it, expect } from 'vitest';
import { mdToHtml } from '../lib/md-to-html.mjs';

describe('mdToHtml', () => {
  it('converts basic markdown', () => {
    const html = mdToHtml('# Title\n\nParagraph.');
    expect(html).toContain('<h1>Title</h1>');
    expect(html).toContain('<p>Paragraph.</p>');
  });

  it('renders info card container', () => {
    const md = '::: info\nTest info.\n:::';
    const html = mdToHtml(md);
    expect(html).toContain('info-card');
  });

  it('renders warning card container', () => {
    const md = '::: warning\nTest warning.\n:::';
    const html = mdToHtml(md);
    expect(html).toContain('warning-card');
  });

  it('preserves Polish diacritics', () => {
    const html = mdToHtml('Bezpieczeństwo pracy ząb ręką.');
    expect(html).toContain('ząb ręką');
  });

  it('preserves UTF-8 special chars (°C, CO₂)', () => {
    const html = mdToHtml('Temperatura 180°C, stężenie CO₂.');
    expect(html).toContain('180°C');
    expect(html).toContain('CO₂');
  });
});
