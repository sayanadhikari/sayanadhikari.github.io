# sayanadhikari.github.io

Personal website of Sayan Adhikari, served by GitHub Pages at https://sayanadhikari.github.io.

## Updating content

Almost everything lives in `_data/`, so most updates are a YAML edit:

| File | What it holds |
| --- | --- |
| `_data/profile.yml` | Name, role, tagline, contact, links, Google Scholar numbers |
| `_data/research.yml` | The four research themes (home and research pages) |
| `_data/cv.yml` | Experience, education, skills, codes, talks, service |
| `_data/publications.yml` | Publication list, newest first. Set `featured: true` to show one on the home page |
| `_data/topics.yml` | Topic labels used for publication filters |

Pages: `index.html` (home and projects), `research.html`, `publications.html`, `cv.html`, `teaching.html`.
Design: `assets/css/site.css`. The hero particle simulation is `assets/js/plasma.js`.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.
