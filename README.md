# diovandi.com

Personal portfolio and blog for [diovandi.com](https://diovandi.com), published automatically with GitHub Pages.

The site is deliberately simple: projects and blog posts are Markdown files, while the shared design lives in a small set of layouts and one stylesheet.

## Edit the home page

Most home-page text is in [`_data/profile.yml`](_data/profile.yml). Edit that file in GitHub, click **Commit changes**, and GitHub Pages will publish the update.

The longer About page is [`about.md`](about.md). The experience timeline is in [`_data/experience.yml`](_data/experience.yml).

## Add a blog post

1. Copy [`templates/post.md`](templates/post.md).
2. Save it in `_posts`.
3. Name it `YYYY-MM-DD-short-title.md`, for example `2026-08-03-my-first-post.md`.
4. Replace the sample front matter and write the post in Markdown.
5. Commit the file. It will appear on the home page and `/blog/`.

## Add a project

1. Copy [`templates/project.md`](templates/project.md).
2. Save it in `_projects` with a short filename such as `robot-arm.md`.
3. Update the title, summary, year, tools, and links.
4. Write the project story below the second `---`.
5. Commit the file. It will appear on `/projects/`. Set `featured: true` to also show it on the home page.

Use `order` to control project order: lower numbers appear first.

## Add research or technical writing

1. Copy [`templates/publication.md`](templates/publication.md).
2. Save it in `_publications`.
3. Set `kind` and `status` honestly—for example, `Course scientific paper`, `Bachelor's thesis`, or `Manuscript / preprint`.
4. Add authors, venue, year, and the summary.
5. Commit the file. It will appear on `/publications/`.

## Add images

Create a folder under `assets/images`, upload the image, and reference it from Markdown:

```md
![Description of the image](/assets/images/example.jpg)
```

Keep images reasonably small (ideally under 500 KB) so the site stays fast.

## Collect portfolio material

Use [`CONTENT_CHECKLIST.md`](CONTENT_CHECKLIST.md) to collect project images, engineering evidence, publication details, permissions, and profile material. It includes a dedicated D03 morphing-leading-edge checklist.

## Preview locally (optional)

Install Ruby and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000`.

## Structure

```text
_data/profile.yml   Home-page text and profile links
_data/experience.yml Experience timeline
_posts/             Blog posts
_projects/          Portfolio entries
_publications/      Research, papers, and technical reports
_layouts/           Shared page templates
_includes/          Header, footer, and cards
assets/css/         Site design
templates/          Copyable post and project starters
```

GitHub Pages publishes from the `main` branch. The `CNAME` file connects the custom domain.
