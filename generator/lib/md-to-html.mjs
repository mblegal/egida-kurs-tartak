import MarkdownIt from 'markdown-it';
import mdContainer from 'markdown-it-container';
import mdAttrs from 'markdown-it-attrs';

export function createRenderer() {
  const md = new MarkdownIt({ html: true, linkify: true, typographer: false });
  md.use(mdAttrs);
  const cards = ['info', 'warning', 'tip', 'example', 'formula'];
  for (const name of cards) {
    md.use(mdContainer, name, {
      render(tokens, idx) {
        if (tokens[idx].nesting === 1) {
          return `<div class="${name}-card">\n`;
        }
        return '</div>\n';
      },
    });
  }
  return md;
}

const renderer = createRenderer();

export function mdToHtml(markdown) {
  return renderer.render(markdown);
}
