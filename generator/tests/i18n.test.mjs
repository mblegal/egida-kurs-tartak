import { describe, it, expect } from 'vitest';
import { pickLang, renderMultilingual } from '../lib/i18n.mjs';

describe('pickLang', () => {
  it('returns requested language if available', () => {
    expect(pickLang({ pl: 'A', en: 'B', es: 'C', uk: 'D' }, 'es')).toBe('C');
  });

  it('falls back to default if missing', () => {
    expect(pickLang({ pl: 'A' }, 'uk', 'pl')).toBe('A');
  });

  it('returns empty string if fallback also missing', () => {
    expect(pickLang({}, 'es', 'pl')).toBe('');
  });
});

describe('renderMultilingual', () => {
  it('wraps all 4 variants with data-lang attributes', () => {
    const html = renderMultilingual(
      { pl: '<p>PL</p>', en: '<p>EN</p>', es: '<p>ES</p>', uk: '<p>UK</p>' }
    );
    expect(html).toContain('data-lang="pl"');
    expect(html).toContain('data-lang="en"');
    expect(html).toContain('data-lang="es"');
    expect(html).toContain('data-lang="uk"');
    expect(html).toContain('<p>PL</p>');
  });
});
