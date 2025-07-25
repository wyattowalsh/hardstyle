This file is a merged representation of a subset of the codebase, containing specifically included files, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: **/*.{md,markdown,mdx,rst,rest,txt,adoc,asciidoc}
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
.changeset/
  chubby-worms-shave.md
  itchy-kings-flash.md
  loud-apples-stay.md
  slick-dolls-act.md
  sour-teeth-deny.md
.github/
  contributing.md
apps/
  docs/
    app/
      (home)/
        blog/
          test/
            page.mdx
    content/
      blog/
        2024-5-15.mdx
        2024-5-16.mdx
        customise-ui.mdx
        make-a-blog.mdx
        mdx-v10-summary.mdx
        mdx-v10.mdx
        new-conventions.mdx
        openapi-v9.mdx
        v12-after.mdx
        v12.mdx
        v13.mdx
        v14.mdx
        v15-2.mdx
        v15.mdx
        why-docs.mdx
      docs/
        cli/
          index.mdx
        headless/
          components/
            breadcrumb.mdx
            index.mdx
            link.mdx
            sidebar.mdx
            toc.mdx
          content-collections/
            index.mdx
          mdx/
            headings.mdx
            index.mdx
            install.mdx
            rehype-code.mdx
            remark-admonition.mdx
            remark-image.mdx
            remark-ts2js.mdx
            structure.mdx
          search/
            algolia.mdx
            index.mdx
            mixedbread.mdx
            orama-cloud.mdx
            orama.mdx
            trieve.mdx
          utils/
            find-neighbour.mdx
            get-toc.mdx
            git-last-edit.mdx
            index.mdx
          custom-source.mdx
          index.mdx
          internationalization.mdx
          page-conventions.mdx
          page-tree.mdx
          source-api.mdx
        mdx/
          (integrations)/
            vite/
              react-router.mdx
              tanstack.mdx
            next.mdx
          async.mdx
          collections.mdx
          global.mdx
          include.mdx
          index.mdx
          last-modified.mdx
          mdx.mdx
          page.mdx
          performance.mdx
        openapi/
          index.mdx
        ui/
          (integrations)/
            openapi/
              configurations.mdx
              index.mdx
              media-adapters.mdx
              proxy.mdx
            feedback.mdx
            llms.mdx
            open-graph.mdx
            python.mdx
            rss.mdx
            typescript.mdx
          components/
            accordion.mdx
            auto-type-table.mdx
            banner.mdx
            dynamic-codeblock.mdx
            files.mdx
            github-info.mdx
            image-zoom.mdx
            index.mdx
            inline-toc.mdx
            steps.mdx
            tabs.mdx
            type-table.mdx
          layouts/
            docs.mdx
            home-layout.mdx
            notebook.mdx
            page.mdx
            root-provider.mdx
          markdown/
            index.mdx
            math.mdx
            mermaid.mdx
            twoslash.mdx
          mdx/
            codeblock.mdx
            index.mdx
          navigation/
            index.mdx
            links.mdx
            sidebar.mdx
          search/
            .shared.mdx
            .tag-filter.mdx
            algolia.mdx
            index.mdx
            mixedbread.mdx
            orama-cloud.mdx
            orama.mdx
          comparisons.mdx
          customisation.mdx
          index.mdx
          internationalization.mdx
          manual-installation.mdx
          page-conventions.mdx
          static-export.mdx
          theme.mdx
          versioning.mdx
          what-is-fumadocs.mdx
      shared/
        page-conventions.i18n.mdx
    public/
      robots.txt
examples/
  content-collections/
    content/
      docs/
        index.mdx
        test.mdx
  i18n/
    content/
      docs/
        index.cn.mdx
        index.mdx
        test.mdx
  next-mdx/
    content/
      docs/
        index.mdx
        test.mdx
        test2.mdx
  openapi/
    content/
      docs/
        auth.mdx
        index.mdx
    README.md
  python/
    content/
      docs/
        index.mdx
    README.md
  react-router/
    content/
      docs/
        index.mdx
        test.mdx
        test2.mdx
  react-router-i18n/
    content/
      docs/
        index.cn.mdx
        index.mdx
        test.mdx
  remote-mdx/
    content/
      docs/
        comparisons.mdx
        index.mdx
        test.mdx
  tanstack-start/
    content/
      index.mdx
      test.mdx
  README.md
packages/
  cli/
    CHANGELOG.md
  content-collections/
    CHANGELOG.md
    README.md
  core/
    test/
      fixtures/
        rehype-toc.md
        remark-admonition.md
        remark-admonition.output.mdx
        remark-heading.md
        remark-image-public-dir.md
        remark-image-public-dir.output.mdx
        remark-image-without-import.output.mdx
        remark-image.md
        remark-steps.md
        remark-steps.output.md
        remark-structure.md
    CHANGELOG.md
    README.md
  create-app/
    template/
      +next/
        content/
          docs/
            index.mdx
            test.mdx
        README.md
      +next+fuma-docs-mdx/
        README.md
      react-router/
        content/
          docs/
            index.mdx
            test.mdx
        README.md
      tanstack-start/
        content/
          index.mdx
          test.mdx
        README.md
    CHANGELOG.md
    README.md
  doc-gen/
    test/
      fixtures/
        file-gen.md
        file-gen.output.md
        file-gen.relative.md
        file-gen.relative.output.md
        remark-install-persist.md
        remark-install.md
        remark-show.mdx
        sample.txt
        ts2js.md
    CHANGELOG.md
    README.md
  mdx/
    test/
      fixtures/
        index.mdx
    CHANGELOG.md
  mdx-remote/
    test/
      fixtures/
        file.mdx
        index.mdx
    CHANGELOG.md
  openapi/
    test/
      out/
        museum/
          events.mdx
          operations.mdx
          tickets.mdx
        unkey/
          apis.mdx
          keys.mdx
          liveness.mdx
          migrations.mdx
          ratelimits.mdx
        petstore.mdx
    CHANGELOG.md
  python/
    CHANGELOG.md
  twoslash/
    CHANGELOG.md
    README.md
  typescript/
    test/
      fixtures/
        test.mdx
    CHANGELOG.md
    README.md
  ui/
    CHANGELOG.md
    README.md
README.md
```

# Files

## File: .changeset/chubby-worms-shave.md
`````markdown
---
'fumadocs-ui': patch
---

Change sidebar direction
`````

## File: .changeset/itchy-kings-flash.md
`````markdown
---
'create-fumadocs-app': patch
---

Update Tanstack Start & React Router templates to use Fumadocs MDX
`````

## File: .changeset/loud-apples-stay.md
`````markdown
---
'fumadocs-ui': patch
---

Ignore IME composition to avoid accidental selection
`````

## File: .changeset/slick-dolls-act.md
`````markdown
---
'fumadocs-mdx': patch
---

Support Tanstack Router/Start via `createClientLoader`
`````

## File: .changeset/sour-teeth-deny.md
`````markdown
---
'fumadocs-core': patch
---

Add mixedbread integration
`````

## File: .github/contributing.md
`````markdown
## Contributing Guide

We greatly appreciate your willingness to contribute to this project!
Before submitting a pull request, there are some guidelines you should notice.

### Guidelines

This project is a monorepo using Turborepo, pnpm and
[Changesets](https://github.com/changesets/changesets). 

#### Before Submitting

- Check if there's other similar PRs.
- Format your code with `pnpm run prettier`.
- Add changesets with `pnpm changeset`, which documents the changes you've made.
- Run unit tests with `pnpm test` and update snapshots if necessary.

#### New Feature

Before submitting a new feature, make sure to open an issue (Feature Request) with sufficient information and reasons about the new feature.
After the feature request is approved, you can submit a pull request.

#### Bug Fixes

Provide a detailed description of the bug (with live demo if possible).
OR open a bug report and link it in your PR.

#### Docs

Contributing to the docs is relatively easier, make sure to check the typos and grammatical mistakes before submitting. 

### New to contributing?

You may start with contributing to the docs,
it is located in `/apps/docs/content/docs`.

To run the docs site in dev mode,
build the dependencies with `pnpm run build --filter=./packages/*` and run `pnpm run dev --filter=docs` to start the dev server.

You don't need any extra environment variables to run this project.
`````

## File: apps/docs/app/(home)/blog/test/page.mdx
`````
export { withArticle as default } from 'fumadocs-ui/page';

## Hello World

Create a `page.mdx` file, put the page under a non-docs layout.

Apply typography styles with:

```jsx
export { withArticle as default } from 'fumadocs-ui/page';
```

Done!
`````

## File: apps/docs/content/blog/2024-5-15.mdx
`````
---
title: How Fumadocs works
description: The framework for building documentation
author: Fuma Nama
date: 2024-05-15
---

1 year ago, I was having fun with Next.js App Router.
While experimenting with it on my toy [No Deploy](https://nodeploy-neon.vercel.app), I planned to build documentation.
However, Nextra does not support App Router.

To handle this, I implemented a small documentation site with solely Contentlayer and the new features from App Router.
It was working great, looked blazing-fast and minimal.
I cloned the logic from No Deploy and built this documentation framework.
With a few months of development, it soon became powerful and stable.

It was originally named `next-docs`, I renamed it to Fumadocs as it conflicts with Next.js Docs.

Thanks to the support from **Next.js** community, I've received a lot of suggestions along the way.
[Fumadocs](https://fumadocs.vercel.app) is now a framework used by my libraries and some other amazing projects.

## My Opinion

In Web development, most _"robust"_ frameworks/libraries are incredibly heavy and fabulous, but it has indeed made our developer experience fancy.

On top of Javascript, people built bundlers, transpilers, and even Typescript.
It feels very surprising that Javascript, a high-level scripting language, is more similar to assembly code in modern Web development.
We rarely use them without things like Webpack. This also applies to CSS, at least in my experience, I seldom use CSS without PostCSS.

While they might be necessary for compatibility and DX, the landing of React Server Component and Next.js App Router made the experience even more mindblowing.
It feels like magic. These cunning magical frameworks, and web development miracles.
This kind of design is insane, but it also makes us mindlessly forget the boundaries.

Beginners use Metadata API, while they have no idea how meta tag works.
They put server-side logic in a server component, while they have no idea how expensive the calculation is.
Even when we looked at the code, we can't predict the result without running it in production mode.
I saw too many of these misconceptions.

This happens on many frameworks, they are overly magical.
**I wanted to make it less-magic, and straightforward at least for most Next.js developers.**

## Fumadocs MDX

As the recommended content source, It is actually a webpack hack.
Since Next.js could only optimize static imports, it first transforms your `.map.ts` to a file that roughly yields:

```ts
export default [import("./my/file.mdx"), ...];
```

And then transforms MDX files with a custom loader. It makes all magic possible, but it doesn't have the ability of lazy-loading MDX files.
Comparing to Nextra, it might be a suboptimal approach.

Nextra does it even easier, it directly transforms MDX files into pages. Because the Pages Router adapts Javascript files as a single page, it is possible.
In App Router, this is not possible anymore. Therefore, I didn't take this approach.

## Fumadocs Core

The core of Fumadocs is a bunch of utilities and MDX plugins.

- **Source API** construct page trees from content source, integrated with other content providers.
- **Headless components** accelerate Fumadocs UI and other custom UI implementations.
- **MDX plugins** bring a perfect developer experience to all integrations.
- **Search utilities** make it way easier to implement document search.

In addition, it has also established the definitions of Page Tree and Page Conventions.
Overall, it is not yet a framework without Fumadocs UI.

In my opinion, the most valuable part of the codebase is MDX plugins.
I learned a lot more about ASTs and the eco-system of remark/rehype while working on them.
Absolutely an amazing experience.

## Fumadocs UI

The UI implementation of Fumadocs using Tailwind CSS and Radix UI.
Its design system was inspired by Shadcn UI, using CSS variables for color utilities.

Although the structure of Fumadocs UI is even simpler than core, I've used some subtle hacks to solve the problem of `"use client"` directive.
The bundler I am using, [TSX](https://github.com/privatenumber/tsx), can't handle nested structures like client components imported from a server component.
Therefore, I made a little hack to build server components and client components as an individual entry, then inject import statements after the process.

Also it took me some time to come up with the [preset approach](https://fumadocs.vercel.app/docs/ui/theme#docsui-plugin) for integrating Fumadocs UI with Tailwind CSS projects.

## Docs Generators

We have a few built-in integrations, like `fumadocs-openapi` which takes an OpenAPI schema and output MDX files.

For the OpenAPI one, it simply parses the schema and convert it to MDX file through string templates.

The Typescript integration does a bit more, it obtains type information with [Typescript Compiler API](https://github.com/Microsoft/TypeScript/wiki/Using-the-Compiler-API). Based on the information, it yields MDX files.
You can use it inside a server component, which is how `<AutoTypeTable />` works.

## CI/CD

As a project with very few contributors, I built the CI/CD process as convenient as possible for a better efficiency.
The entire release process is handled by [Changesets](https://github.com/changesets/changesets), and I wrote the scripts to update [the template repository](https://github.com/fuma-nama/fumadocs-ui-template) automatically.
It worked great so far.

## Thanks

[The Github repository of Fumadocs](https://github.com/fuma-nama/fumadocs) has reached 300 stars in 2024 March, it is a new achievement for me.
Welcome to give it a star to support my work!

> Original
> https://fuma-nama.vercel.app/blog/fumadocs
`````

## File: apps/docs/content/blog/2024-5-16.mdx
`````
---
title: 500 Stars
description: The first 500 stars of Fumadocs
author: Fuma Nama
date: 2024-05-16
---

It was surprising when I first saw [the video from Web Dev Cody](https://youtu.be/7HUmDAgXI2E?si=CR9fC-f3nysPJJCE), it felt like I had finally built something worth mentioning, instead of another neglected side project that nobody cares about.

So far I've worked on this project for about 1 year, and it is a precious experience to me. The best lecture that you can't find in a university.

## Open Source

I received much feedback, issues and questions. Some are brutal but straightforward, like _"please fix it, help me please"_ _"Support XXX please"_. Some are kind and helpful, willing to provide a PR.
I felt both the good and bad sides of open source.

Sometimes, people are being eager and impulsive because of stress and may spread their frustration on the library maintainers.
Even myself, can be affected by stress or a bad mood.

People may hope for instant answers, and maintainers will face questions like _"Why are you running away from my questions?"_.
I understand a library performing bad can cause your precious time to be wasted, but even if we put all our efforts in maintaining the library, it can't be flawless.

Since then, I feel I'm way more respectful to open-source project maintainers.
At least, I'll check my before before firing an issue on somebody else's Github repository, and try to be as respectful as I can ~~with my poor language skills~~.

### Issues

My favourite dev was [Anthony Shew](https://shew.dev), I mentioned him because [the issue he opened](https://github.com/fuma-nama/fumadocs/issues/264) is the best I've ever seen in my open-source career.
He actually cared about my vision and opinion about the API design, and gave a really concise and constructive feature request.

Obviously, I was not a perfect, neither an experienced library dev.
Fumadocs wasn't capable of many things, such a well-explained feature request and idea is powerful. His passion is inspiring.

Before setting up the YAML issue template, there were very few issues that actually followed the issue template, most of them don't even provide a reproducible repository, or an explanation.

**Open a proper issue, follow the instructions, and give maintainers some positive feedback.** This is the biggest motivation you can give to maintainers without specnding money.

## Docs

It's fun to work on the docs of fumadocs. When first building it, I had very little experience on authoring documentation and tutorial content.
Reading through the feedback from developers, the most common problem is that they can't find the docs of something.

I realized the entire docs is unfriendly for beginners to start with, my friends are senior Next.js devs, and of course they are fine with that.
However, not every dev can understand the docs.

So recently, I started to re-write some of the sections, making it easier and appealing for beginners. Welcome to share your feedback on Github Discussions!

## What is Next?

Web Development is an ever-evolving industry, but I believe the spirit of open source won't disappear.
I don't know what I will be building in the future, and that doesn't matter.
Let's build a better web!
`````

## File: apps/docs/content/blog/customise-ui.mdx
`````
---
title: Rethink how we customise UI
description: Deep dive on how Fumadocs UI is designed
author: Fuma Nama
date: 2025-04-15
---

## The Problem

Making a docs framework isn't challenging, the hardest problem is how I can make it perfect for everyone, from the perspective of users and developers.
Undoubtedly, this is **a dilemma** for all frameworks, or even library authors — You cannot write generic code that works out-of-the-box, there's no piece of software that is straight usable while being generic.

For example, headless UI libraries like **Radix UI** gave us the concept of generic UI components: bare UI primitives that we can customise according to our aesthetics.
However, you'll need time to tune them, these primitives are unusable without further customisations.

Yep it's 2025, **Shadcn UI** had led a "revolution" on Web Development. It's a great combination of headless UI and styled defaults that takes an extra step away!
But our problem remains unsolved, it might be preposterous that it becomes "unstyled" again when a vast majority of new sites adopted Shadcn UI.

Personally, I felt overwhelmed by nearly identical, ubiquitous flat designs that are obviously one of the default Shadcn UI styles. It has nothing to do with Shadcn UI, but the rest of developers who don't actually care about aesthetics and uniqueness.
Eventually, **Shadcn-like design became the default styles**, so once again, we will need to do a bit more to make it look stylish.

### What should we do?

As a docs framework started from **"being flexible"**, Fumadocs must be customisable, tuned to meet developers' preferences.
We will need to take customisation seriously if DX is what we aim. And most importantly, **it should encourage developers with a sense of beauty to customise.**

## The Solution

Typically, there are two types of developers:

### those who want docs that just work

Fumadocs need to be opinionated by default such that it is immediately usable, and we only have to offer simplest options to change details. (e.g. colors, overriding components).

Most developers have no desire to install dozens of components just to change a tiny detail, which makes the Shadcn approach suboptimal.

### those who need the perfect docs tailored to their preferences

The kernel of Fumadocs, or the spirit we're pursuing is the latter one. I crafted Fumadocs CLI, a version of Shadcn UI dedicated for Fumadocs, the whole solution is now simplified into a single command:

```package-install
npx @fumadocs/cli customise
```

It accounts for two types:

- Customise the default styles when the exposed options are inadequate.
- Roll their own layout from scratch.

The first one is self-evident, people will always have absurd needs that we have not even considered.
We can install the original components, so it's simply identical to the default UI which they've been using.

The latter one is simpler, we can offer the minimal template they can start customising from.

This methodology, inspired by ejection, brings some nice advantages:

#### Don't break anything when you upgrade Fumadocs

Fumadocs need to be opinionated. Hence, we need to iterate the UI frequently which apparently will break people's hacky customisations.
The charm of Fumadocs CLI is that once you've installed the layout, it stays the same forever regardless of future iterations on Fumadocs UI.

It gives the courage for Fumadocs UI to iterate, and developers to customise unburnt by the fear of upgrading dependencies.

#### Looks Clean

Just like Shadcn UI and Radix UI, Fumadocs UI has a core package (`fumadocs-core`), most generic logic will be abstracted by core.

## What is Next?

The innovation of Shadcn UI is amazing, yet, I believe there's more problems Fumadocs can solve.

See [Flags SDK](https://flags-sdk.dev/frameworks/next) and [BetterAuth](https://www.better-auth.com/docs/introduction), you can't tell at the first glance if they're powered by Fumadocs.
I hope it can continue to be a "breakable" framework known for how customisable it is.
`````

## File: apps/docs/content/blog/make-a-blog.mdx
`````
---
title: Making a Blog with Fumadocs
description: Fumadocs + Blog
author: Fuma Nama
date: 2024-12-15
---

Fumadocs is a docs framework, but it's also a powerful tool to manage content in Next.js. You can use Fumadocs to build a blog site along with docs, on a single Next.js app.

## Overview

This guide helps you build a blog site with Fumadocs and Fumadocs MDX.

We will use Fumadocs MDX to manage the content, and implement our own UI with Tailwind CSS & Fumadocs UI.

### Configure Content

Define a `blogPosts` collection.

```ts title="source.config.ts"
import { defineCollections, frontmatterSchema } from 'fumadocs-mdx/config';
import { z } from 'zod';

export const blogPosts = defineCollections({
  type: 'doc',
  dir: 'content/blog',
  // add required frontmatter properties
  schema: frontmatterSchema.extend({
    author: z.string(),
    date: z.string().date().or(z.date()),
  }),
});
```

Parse the output collection in `source.ts`:

```ts title="lib/source.ts"
import { createMDXSource } from 'fumadocs-mdx';
import { loader } from 'fumadocs-core/source';
import { blogPosts } from '@/.source';

export const blog = loader({
  baseUrl: '/blog',
  source: createMDXSource(blogPosts),
});
```

You can now access the content from `blog`.

### Implement UI

Create an index page for blog posts.

By default, there should be a `(home)` route group with `<HomeLayout />` inside.
Let's put the blog pages under it, this way we can get the nice navbar on our blog site.

```tsx title="app/(home)/blog/page.tsx"
import Link from 'next/link';
import { blog } from '@/lib/source';

export default function Home() {
  const posts = blog.getPages();

  return (
    <main className="grow container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-8">Latest Blog Posts</h1>
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {posts.map((post) => (
          <Link
            key={post.url}
            href={post.url}
            className="block bg-fd-secondary rounded-lg shadow-md overflow-hidden p-6"
          >
            <h2 className="text-xl font-semibold mb-2">{post.data.title}</h2>
            <p className="mb-4">{post.data.description}</p>
          </Link>
        ))}
      </div>
    </main>
  );
}
```

<Callout title='Good to Know'>

Colors like `text-fd-muted-foreground` are from the design system of Fumadocs UI, you may also use your own colors, or use Shadcn UI.

</Callout>

And create a page for blog posts.

Note that blog posts won't have nested slugs like `/slug1/slug2`. We don't need a catch-all route for blog posts.

```tsx title="app/(home)/blog/[slug]/page.tsx"
import { notFound } from 'next/navigation';
import Link from 'next/link';
import { InlineTOC } from 'fumadocs-ui/components/inline-toc';
import defaultMdxComponents from 'fumadocs-ui/mdx';
import { blog } from '@/lib/source';

export default async function Page(props: {
  params: Promise<{ slug: string }>;
}) {
  const params = await props.params;
  const page = blog.getPage([params.slug]);

  if (!page) notFound();
  const Mdx = page.data.body;

  return (
    <>
      <div className="container rounded-xl border py-12 md:px-8">
        <h1 className="mb-2 text-3xl font-bold">{page.data.title}</h1>
        <p className="mb-4 text-fd-muted-foreground">{page.data.description}</p>
        <Link href="/blog">Back</Link>
      </div>
      <article className="container flex flex-col px-4 py-8">
        <div className="prose min-w-0">
          <InlineTOC items={page.data.toc} />
          <Mdx components={defaultMdxComponents} />
        </div>
        <div className="flex flex-col gap-4 text-sm">
          <div>
            <p className="mb-1 text-fd-muted-foreground">Written by</p>
            <p className="font-medium">{page.data.author}</p>
          </div>
          <div>
            <p className="mb-1 text-sm text-fd-muted-foreground">At</p>
            <p className="font-medium">
              {new Date(page.data.date).toDateString()}
            </p>
          </div>
        </div>
      </article>
    </>
  );
}

export function generateStaticParams(): { slug: string }[] {
  return blog.getPages().map((page) => ({
    slug: page.slugs[0],
  }));
}
```

And configure metadata:

```tsx title="app/(home)/blog/[slug]/page.tsx"
import { notFound } from 'next/navigation';
import { blog } from '@/lib/source';

export async function generateMetadata(props: {
  params: Promise<{ slug: string }>;
}) {
  const params = await props.params;
  const page = blog.getPage([params.slug]);

  if (!page) notFound();

  return {
    title: page.data.title,
    description: page.data.description,
  };
}
```

### Write Posts

The UI is now complete, you can write some blog posts under the `content/blog` directory, like:

```mdx title="content/blog/hello.mdx"
---
title: Hello World
author: Fuma Nama
date: 2024-12-15
---

## Hello World

This is an example!
```

After spinning up the development server with `next dev`, you should see the blog posts under `/blog` route.
`````

## File: apps/docs/content/blog/mdx-v10-summary.mdx
`````
---
title: Fumadocs MDX v10 Summary
description: Migration Guide and Summary
date: 2024-11-24
author: Fuma Nama
---

## Features

- More customisations via `source.config.ts`, a new config file for your content.
- Introduced **collections**.
- Turbopack support.
- Build-time data validation support.

## Migrate from v9

### Refactor Imports

Refactor the import in `next.config`.

**From:**

```ts
import createMDX from 'fumadocs-mdx/config';

const withMDX = createMDX();

/** @type {import('next').NextConfig} */
const config = {
  reactStrictMode: true,
};

export default withMDX(config);
```

**To:**

```ts
import { createMDX } from 'fumadocs-mdx/next';

const withMDX = createMDX();

/** @type {import('next').NextConfig} */
const config = {
  reactStrictMode: true,
};

export default withMDX(config);
```

### Remove `mdx-components.tsx`

`mdx-components.tsx` is no longer used. It now allows only MDX components passed from `MDX` body's `components` prop.

```tsx
import defaultMdxComponents from 'fumadocs-ui/mdx';

const MDX = page.data.body;

// set your MDX components with `components` prop
<MDX components={{ ...defaultMdxComponents }} />;
```

This encourages explicit import of MDX components.

Previously, `mdx-components.tsx` worked by injecting an import to every compiled Markdown/MDX file.
It's somewhat unnecessary because you can always import the components explicitly, or replace default HTML tags like `img` from MDX body's `components` prop.

### Define Collections

Collection is now introduced on source config file (`source.config.ts`).
It refers to a collection of files/content, such as Markdown files or JSON/YAML files.

Every collection has its own config, you can have customised Zod schema to validate its data, or collection-level MDX options for content collections.

You can create a source config file, and add the following:

```ts
import { defineDocs } from 'fumadocs-mdx/config';

export const { docs, meta } = defineDocs({
  dir: 'content/docs',
});
```

`defineDocs` declares two collections, one with `doc` type that scans content files (e.g. `md/mdx`), one with `meta` type that scans meta files (e.g. `json`).

Now you can generate types using `fumadocs-mdx` command, it's recommended to set it as a `postinstall` script.

```json title="package.json"
{
  "scripts": {
    "postinstall": "fumadocs-mdx"
  }
}
```

When starting the development server, a `.source` folder will be generated, it contains all parsed collections/files.
You can add it to `.gitignore`, it will replace the old `.map` file.

To access the collections, import them from the folder with their original name in `source.config.ts`.

```ts
import { docs, meta } from '@/.source';
```

Now to integrate it with Fumadocs framework, change your `source.ts` from:

```ts
import { map } from '@/.map';
import { createMDXSource } from 'fumadocs-mdx';
import { loader } from 'fumadocs-core/source';

export const { getPage, getPages, pageTree } = loader({
  baseUrl: '/docs',
  rootDir: 'docs',
  source: createMDXSource(map),
});
```

to:

```ts
import { docs, meta } from '@/.source';
import { createMDXSource } from 'fumadocs-mdx';
import { loader } from 'fumadocs-core/source';

export const source = loader({
  baseUrl: '/docs',
  source: createMDXSource(docs, meta),
});
```

- we now recommend exporting the output of `loader` directly as a single variable.
- schema option is no longer defined in `source.ts`, it's handled by `source.config.ts`.
- it takes two collections: `docs` (content) and `meta` (`meta.json`).
  You can leave `meta` as an empty array if it is unused, so you can define only a collection for `docs`.

### `page.data`

When using with `loader`, you no longer need `data.frontmatter` to access frontmatter data.
It is merged into the `page.data` object.

```ts
page.data.frontmatter.title; // [!code --]
page.data.title; // [!code ++]
```

### MDX Options

Instead of passing them to `next.config` file, define a global config in `source.config.ts`:

```ts
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    // here!
  },
});
```

### Collection Schema

The `schema` option of collection allow you to customise the validation schema, it accepts a Zod type.

For `defineDocs`, see [`schema`](/docs/mdx/collections#schema-1).

### Multiple Types

Same as before, you can call `loader` multiple times for different types (e.g. for docs and blog).

```ts
import { createMDXSource } from 'fumadocs-mdx';
import type { InferMetaType, InferPageType } from 'fumadocs-core/source';
import { loader } from 'fumadocs-core/source';
import { meta, docs, blog as blogPosts } from '@/.source';

export const source = loader({
  baseUrl: '/docs',
  source: createMDXSource(docs, meta),
});

export const blog = loader({
  baseUrl: '/blog',
  // as mentioned before, you can leave `meta` an empty array
  source: createMDXSource(blogPosts, []),
});

export type DocsPage = InferPageType<typeof source>;
export type DocsMeta = InferMetaType<typeof source>;
```

and the corresponding `source.config.ts`:

```ts
import {
  defineDocs,
  defineCollections,
  frontmatterSchema,
} from 'fumadocs-mdx/config';
import { z } from 'zod';

export const { docs, meta } = defineDocs({
  dir: 'content/docs',
});

export const blog = defineCollections({
  type: 'doc',
  dir: 'content/blog',
  schema: frontmatterSchema.extend({
    author: z.string(),
    date: z.string().date().or(z.date()).optional(),
  }),
});
```

### Further Readings

You can read the latest docs of Fumadocs MDX for details.

<Cards>
  <Card href="/docs/mdx" title="Fumadocs MDX">
    The built-in content source, build a better content experience on Next.js.
  </Card>
</Cards>
`````

## File: apps/docs/content/blog/mdx-v10.mdx
`````
---
title: Fumadocs MDX v10
description: Improvement over Fumadocs MDX, our built-in content source.
date: 2024-09-06
author: Fuma Nama
---

## The Problem

Fumadocs MDX worked great for docs. But we also want to prioritize flexibility and code organization.

Previously, it was a simple Webpack loader that turns **MDX** into **JavaScript**.
You pass the MDX processor options to the loader, it turns them into JavaScript files.
Then, a `.map.ts` will be exported:

```ts
export const map = {
  'docs/index.mdx': import('./docs/index.mdx'),
  'docs/guide.mdx': import('./docs/guide.mdx'),
};
```

Your Next.js app will import the map file, and access the available MDX files.

This model works, but we started to see some problems:

- **No built-in way to define multiple collections:**

  For example, we have a directory for blog posts and a directory for docs pages.

  On Fumadocs MDX, all these resources are transformed into a single object exported by `.map.ts`:

  ```ts
  export const map = {
    'blog/post.mdx': import('./blog/post.mdx'),
    'docs/index.mdx': import('./docs/index.mdx'),
  };
  ```

  We implemented a solution using Source API `rootDir` option, but this is not the ideal way.
  This also gave us another problem:

- **Different MDX Options for each collection:**

  Same as the above example, we have a `/blog` directory for blog posts.
  If we want to add a remark plugin that **only work on blog posts**, this is impossible with Fumadocs MDX.

  Once you apply a remark plugin, it's effective on all MDX files, including the MDX files in the docs directory.

- **Turbopack Compatibility:**

  Turbopack doesn't allow passing unserializable options to loaders.
  However, the entire MDX, remark and rehype ecosystem use functions for plugins.
  Functions are not serializable, we cannot migrate Fumadocs to Turbopack unless we find a seamless solution that supports Turbopack.

- **Compile-time validation:**

  All schema validation cannot be done during build time because the MDX loader actually, _doesn't know the collections you defined in `source.ts`._

  Furthermore, the Zod schema is passed to the source adapter in `source.ts` rather than the loader:

  ```ts
  import { loader } from 'fumadocs-core/source';
  import { createMDXSource } from 'fumadocs-mdx';

  export const source = loader({
    source: createMDXSource(map, {
      // schema
    }),
  });
  ```

  This loses some performance optimizations that can be possibly done on bundler level.

- **Untyped:**

  The exported `map` object from `.map.ts` file has a type of `unknown`, it is only typed when using it with Source API `loader`.

  This avoided the complexity to auto-generate types, but I wanted to make it typed and usable without Source API.

### The Solution

Taking some references from Content Collections and [Velite](https://velite.js.org), I found it would be great to have a config file for Fumadocs MDX.

#### `source.config.ts`

We can make the syntax similar to Content Collections and other tools, to make the adoption process easier.
To define a collection:

```ts
import { z } from 'zod';

export const blog = defineCollections({
  dir: './blog',
  schema: z.object({
    // the schema
  }),
  mdxOptions: {
    // remark plugins?
  },
});
```

The MDX loader reads the config file, find the corresponding collection of the file, validate, and compile it using the options from collection.

This allows us to pass MDX options normally without breaking Turbopack's rules.

### The Implementation

As the config file is written in TypeScript, we will need a bundler to read it.
I used esbuild, it is a performant bundler written in Go.

After bundling the config file, a dynamic import will work as expected.

```js
await import('./source.compiled.mjs');
```

#### `.map` file

We need a place to import the compiled collections.
Previously, we simply generate a `.map.ts` file with Webpack plugins.
It declares the types, with no actual data.

```ts
export declare const map: unknown;
```

A loader will be used to transform `.map.ts` file into the output aforementioned:

```ts
export const map = {
  'docs/index.mdx': import('./docs/index.mdx'),
  'docs/guide.mdx': import('./docs/guide.mdx'),
};
```

The generated `.map.ts` never changes because it doesn't depend on the config file.
No matter how you configure it, there'll be only a `map` object exported, with a type of `unknown`.

Now, we need to generate types for every collection, and the types may change as we change the collections.
The previous approach is no longer applicable.

I renamed the `.map.ts` file to `.source/index`, both `index.d.ts` and `index.js` are generated by Fumadocs MDX, instead of using a loader.

A map file generator is implemented, it reads the config file and generate output based on exported collections.

#### Auto-reload

We want to watch for changes:

- When a input file added/removed, add or remove relevant entries from the `.source/index.js` file.
- When the config file changed, re-compile affected files, and update generate types at `.source/index.d.ts`.

I chose chokidar to watch file changes, it worked well.
The file watcher lives on `next.config.mjs`, it's independent to the MDX loader.

To notify bundlers when config files changed, we added a **hash**.

```ts
export const collection1 = [import('./docs/index.mdx?hash=hashOfConfigFile')];
```

The file will be re-compiled as the config hash changes.

To optimize performance, we also added the collection name.

```ts
export const collection1 = [
  import('./docs/index.mdx?hash=hashOfConfigFile&collection=collection1'),
];
```

The loader obtains the collection of input file from resource query, without taking extra steps to detect its associated collection.

### Result

A `.source/index` file will be generated, it is fully typed.
The files will be re-compiled as you modify the config file.

- Turbopack supported, we have a small example in the repo using Turbopack.
- Multiple Collections, with its own MDX options.
- Runtime + Build-time validation & transformation.

### Questions

I think there is still room for improvement:

- Use a Turbopack-native thing to bundle the config file?
- Lazy bundle/import the main body of MDX file?

Please give me feedback about the redesign of Fumadocs MDX ;)
`````

## File: apps/docs/content/blog/new-conventions.mdx
`````
---
title: Adding new Conventions
description: Some changes on the docs.
date: 2025-04-08
author: Fuma Nama
---

## `mdx-component.tsx`

Sometimes there are questions raised by beginners confused about where to add MDX components.
Although it's simply located in `page.tsx`, which shouldn't be difficult to find, I think some kind of conventions may help, so I decided to add back `mdx-components.tsx`.

I love to have fewer files, but considering `create-fumadocs-app` should also act as a starting point for beginners who may not be familiar with MDX, it's much more helpful to provide it by default.

### Existing Projects

The convention is optional (only to make the learning curve smoother).
For existing users, you probably knew how to pass MDX components, and no further change is needed.

But you can still make one:

```tsx title="mdx-components.tsx"
import defaultMdxComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultMdxComponents,
    ...components,
  };
}
```

And use it in your MDX component.

```tsx title="page.tsx"
import { getMDXComponents } from '@/mdx-components';

<MDXContent
  components={getMDXComponents({
    // extend it
  })}
/>;
```

## Deprecating `<I18nProvider />`

We now prefer a single `<RootProvider />` for everything, replacing the need for `<I18nProvider />` with a `i18n` prop.

```tsx
<RootProvider
  i18n={
    // i18n provider props
  }
>
  {children}
</RootProvider>
```

This allows Root Provider to handle the hierarchy correctly without revealing too much complexity, for example, the correct order should be:

```tsx
<FrameworkProvider>
  <ThemesProvider>
    <I18nProvider>
      <SidebarProvider>
        <SearchProvider>{children}</SearchProvider>
      </SidebarProvider>
    </I18nProvider>
  </ThemesProvider>
</FrameworkProvider>
```

Changing the hierarchy of different providers may result in problems since they actually rely on each other, now it is all integrated into `<RootProvider />`, including I18n configuration.

The new [Internationalization](/docs/ui/internationalization) guide requires Fumadocs 15.2.3 or above.
`````

## File: apps/docs/content/blog/openapi-v9.mdx
`````
---
title: Fumadocs OpenAPI v9
description: Better UI & DX
date: 2025-05-25
author: Fuma Nama
---

## Overview

This breaking change is mainly made to address problems of `generateFiles()` function.

Previously, it was a simple function to generate multiple MDX files/pages from your OpenAPI schema, same as every docs generator.
We tested it on public OpenAPI schemas such as Unkey, Vercel and examples from Scalar and Swagger's Museum schema.

Since these schemas were written for different docs solutions, or even their custom ones.
We made `generateFiles()` too complicated to be capable of producing best results for various schema styles, and it's even harder to customise the generated file paths of API docs.

This update also include:

- Better UI for schema & playground body input
- Improved type-safety for `generateFiles()`

## Breaking Changes

The algorithm for generating file paths is changed:

- `meta.json` will no longer be generated, add as your wanted.
- `per: operation`: The generated path will be identical to your operation id. If not defined, it takes your endpoint path instead.

### Group By

The behaviour of `groupBy` API is also changed.

| value | output                                                 |
| ----- | ------------------------------------------------------ |
| tag   | `{tag}/{operationId ?? endpoint_path}.mdx`             |
| route | `{endpoint_path}/{method}.mdx` (ignores `name` option) |
| none  | `{operationId ?? endpoint_path}.mdx` (default)         |

### Customise Output

The usage of `name` option is renewed, it can be used to customise the output path of files.

```ts
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  name: (output, document) => {
    // page info
    console.log(output);
    // parsed OpenAPI schema
    console.log(document);
    return 'my-dir/filename';
  },
});
```

## Migration

You can start using the latest algorithm, or keep the current behaviour with:

```ts
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  name: {
    algorithm: 'v1',
  },
});
```

Note that it won't create `meta.json` anymore even with `algorithm` set to `v1`, you can keep your current generated `meta.json` files.
`````

## File: apps/docs/content/blog/v12-after.mdx
`````
---
title: Fumadocs 12.0.5
description: After the release of Fumadocs 12
date: 2024-06-13
author: Fuma Nama
---

## Some Improvements

After releasing Fumadocs 12, some improvements were made to the new UI.

### TOC Popover

Previously, this was only available on larger devices. Now, it's collapsed to a popover on smaller devices.

<div className='mx-auto max-w-[400px]'>

![Preview](/blog/toc-popover.png)

</div>

### Links Menu

To make the sidebar look even better, we moved navigation links to the links menu (the three-dots button at the top corner).

The recommended design is:

- Docs related links: Use `<RootToggle />` or include it in page trees.
- Other links: Use the Links API of docs layout.

<div className='mx-auto max-w-[400px]'>

![Preview](/blog/links-menu.png)

</div>

### Breadcrumbs

Removed the duplicated page name from breadcrumbs, now it only shows the folder names.
Also, you can enable `includeSeparators` to show separators on your breadcrumbs component.

The new breadcrumbs look cleaner and match the design even better.

## Adaption

Some docs sites such as https://yeecord.com and https://turbo.build have adopted the new UI, I'm very excited about it.
Removing the navbar seemed to be a very risky move to me, almost no documentation framework has done it, and I was expecting some complaints about the new design.

Luckily, most people are satisfied with the new UI.
The new design was originally inspired by Arc, their sidebar looked very impressive to me.
Although I soon discovered the docs site of Linear also doesn't have a navbar, Arc is still the first inspiration of the redesign.

I'm grateful that many people gave me their feedback about the new design, so that I can keep making Fumadocs a better framework to use.
Let's make better docs.
`````

## File: apps/docs/content/blog/v12.mdx
`````
---
title: Fumadocs 12
description: Introduce Fumadocs v12
date: 2024-06-09
author: Fuma Nama
---

## What's New?

Fumadocs v12 mainly aims to improve the UI, prioritizing content and reading experience.

### New UI

After observing large docs sites like https://turbo.build, I found that the navbar took too much space on the screen, while it only contains links to Blog, Showcase, GitHub, etc.
They are not necessarily related to the docs, placing them at the top of our screen doesn't bring a better reading experience.

All these links are now moved to the sidebar, allowing a clean, minimal view of the docs.

![Preview](/blog/v12.png)

I also noticed the docs start to look messy as your content grows. To ameliorate this, the sidebar now includes a border and background by default.
This helps readers to distinguish navigation elements and content easier.

The sidebar will always be placed at the left of the screen, having a bigger space on large viewports.

I believe the new UI still has room for improvement. Welcome to report UI issues, or leave feedback!

### Better Multi Page Trees

We supported multiple page trees at a very early version of Fumadocs. However, it lacks proper explanations and guides to configure it.
In the past, you needed to implement a navigation element to switch between page trees and mark the folder as a root folder.

Now, you can use the `<RootToggle />` component directly, and the docs has a better explanation of it.

<div className="flex flex-row justify-center mx-auto max-w-[300px]">
  ![Preview](/blog/v12-root-toggle.png)
</div>

### Page Tree Post Processors

You can now attach properties to page trees easily with the Source API.

```ts
import { loader } from 'fumadocs-core/source';

export const utils = loader({
  pageTree: {
    attachFile(node) {
      // modify the node
      return node;
    },
  },
});
```

### Improved i18n Support

The language switch is now added to Docs Layout.

```tsx
import { DocsLayout } from 'fumadocs-ui/layouts/docs';

export default function Layout({ children }: { children: React.ReactNode }) {
  return <DocsLayout i18n>{children}</DocsLayout>;
}
```

Note that `<LanguageSelect />` component is now replaced by `<LanguageToggle />`, make sure to remove references to the old component.

## Breaking

### UI

Remove deprecated option `enableThemeProvider` from Root Provider. Use `theme.enabled` instead.

### Core

Remove deprecated option `minWidth` from Sidebar component. Use `blockScrollingWidth` instead

## Fixes

### UI

- Fix problems with twoslash codeblocks
- Apply typography styles to headings
- Support translation for theme label

### OpenAPI

- Fix nullable types cannot be detected

### Core

- Remark Headings: Support code syntax in headings

### Create Fumadocs App

- Add `layout.config.tsx` file for sharing layout options
`````

## File: apps/docs/content/blog/v13.mdx
`````
---
title: Fumadocs v13
description: Introducing Fumadocs v13
author: Fuma Nama
date: 2024-07-28
---

## Introduction

Fumadocs v13 has been released. It aims to fix the CSS pollution problem and remove deprecated APIs.

## New Features

### Better Code Blocks

Now supports keeping the original background generated by Shiki on `CodeBlock` component.

```tsx
import { Pre, CodeBlock } from 'fumadocs-ui/components/codeblock';

<MDX
  components={{
    pre: ({ ref: _ref, ...props }) => (
      <CodeBlock keepBackground {...props}>
        <Pre>{props.children}</Pre>
      </CodeBlock>
    ),
  }}
/>;
```

### Callout

Callout is now a default MDX component, you can use it in MDX files without an import, or manually adding it to MDX components.

```mdx
<Callout type="warn">Hello World</Callout>
```

### New Headless TOC

The headless component of Table of Contents (TOC) now has a separate scroll container provider.

```tsx
import * as Base from 'fumadocs-core/toc';

return (
  <Base.AnchorProvider>
    <Base.ScrollProvider>
      <Base.TOCItem />
      <Base.TOCItem />
    </Base.ScrollProvider>
  </Base.AnchorProvider>
);
```

The anchor provider can be placed anywhere.

### Opt-out of Container

Now supports disabling the default container styles of Tailwind CSS added by Fumadocs UI.

```js
import { createPreset } from 'fumadocs-ui/tailwind-plugin';

/** @type {import('tailwindcss').Config} */
export default {
  presets: [
    createPreset({
      modifyContainer: false,
    }),
  ],
};
```

### Admonition Syntax

In Docusaurus, there's an [Admonition syntax](https://docusaurus.io/docs/markdown-features/admonitions).

For people migrating from Docusaurus, you can enable the new remark plugin to support the Admonition syntax.

See [Remark Admonition](/docs/headless/mdx/remark-admonition).

## Breaking Changes

### Prefix to colors, animations, and utilities

Previously, the Tailwind CSS plugin of Fumadocs UI added colors (including `primary`, `secondary`) which conflicted with Shadcn UI and other design systems.
A `fd-` prefix is added to them to allow the flexibility to have a separated design system on docs.

To use the Fumadocs UI colors on your primary app, enable the `addGlobalColors` option.

```js
import { createPreset } from 'fumadocs-ui/tailwind-plugin';

/** @type {import('tailwindcss').Config} */
export default {
  presets: [
    createPreset({
      addGlobalColors: true,
    }),
  ],
};
```

This adds the colors without the `fd-` prefix.

Or you can just reference them with the `fd-` prefix, like `bg-fd-background`.

### Tailwind CSS Plugin ESM-only

Since Tailwind CSS supports TypeScript configuration, it makes sense to migrate the entire plugin to ESM.

Use ESM syntax in your configuration.

```ts
import { createPreset } from 'fumadocs-ui/tailwind-plugin';

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './app/**/*.{ts,tsx}',
    // others
  ],
  presets: [createPreset()],
};
```

### Remove `RollButton` component

`RollButton` was introduced because there were no "Table Of Contents" on mobile viewports.
Now users can use the TOC Popover to switch between headings, it is no longer a suitable design for Fumadocs UI.

You may copy the [last implementation of `RollButton`](https://github.com/fuma-nama/fumadocs/blob/fumadocs-ui%4012.5.6/packages/ui/src/components/roll-button.tsx).

### Better i18n

Now the `I18nProvider` component requires the `locale` prop instead of parsing it from pathname.
This fixed some bugs with the I18n middleware.

We also changed the usage of `translations` to reduce extra translations loaded on the client side.
You have to pass the active translations directly.

`locales` is passed as the available options on the Language Select component.

```tsx
import { RootProvider } from 'fumadocs-ui/provider';
import type { ReactNode } from 'react';
import { I18nProvider } from 'fumadocs-ui/i18n';

export default function Layout({
  params: { lang },
  children,
}: {
  params: { lang: string };
  children: ReactNode;
}) {
  return (
    <html lang={lang}>
      <body>
        <I18nProvider
          locale={lang}
          // options
          locales={[
            {
              name: 'English',
              locale: 'en',
            },
            {
              name: 'Chinese',
              locale: 'cn',
            },
          ]}
          // translations
          translations={
            {
              cn: {
                toc: '目錄',
              },
            }[lang]
          }
        >
          <RootProvider>{children}</RootProvider>
        </I18nProvider>
      </body>
    </html>
  );
}
```

### Code Block Usage

The previous usage was confusing, some props are passed directly to `pre` while some are not.

With v13, pass all props to the `CodeBlock` component.
This also includes class names, you may change your custom styles if necessary.

```tsx
import { Pre, CodeBlock } from 'fumadocs-ui/components/codeblock';

<MDX
  components={{
    // HTML `ref` attribute conflicts with `forwardRef`
    pre: ({ ref: _ref, ...props }) => (
      <CodeBlock {...props}>
        <Pre>{props.children}</Pre>
      </CodeBlock>
    ),
  }}
/>;
```

### Remove Deprecated APIs

- Remove deprecated `fumadocs-ui/components/api` components.
- Replace `secondary` link items with `icon` link items.
- Rename `id` prop on Tabs component to `groupId`.

## Bug Fixes

### UI

- Fixed empty folder animation problems caused by Radix UI.
`````

## File: apps/docs/content/blog/v14.mdx
`````
---
title: Fumadocs v14
description: Introducing Fumadocs v14
author: Fuma Nama
date: 2024-09-19
---

## Why?

Taking some inspirations from [Shadcn UI](https://ui.shadcn.com), I decided to make Fumadocs easier to use, with more APIs that simplify the design.

This is a large update.

## New Features

### Fumadocs CLI

Clone Fumadocs UI components to your workspace and modify them.

```package-install
npm install @fumadocs/cli --save-dev
```

```bash
pnpm fumadocs add
```

See [docs](/docs/cli) for details.

### Sidebar Tabs

Previously, multiple page tree is implemented with Fumadocs UI `RootToggle` component.
You have to add it to the sidebar banner which isn't as intuitive as other APIs.

With Sidebar Tabs, by creating a root folder, Fumadocs will immediately add a tabs component to the sidebar.

```json title="meta.json"
{
  "root": true,
  "title": "Tab Name",
  "description": "Some text about the tab",
  "icon": "IconName"
}
```

### Orama

We migrated the built-in search from Flexsearch to Orama, the same search engine that powers the Node.js docs site.
It is open source, and also have their Cloud integration.

No changes required.
You can use our new `createFromSource` API to create the route handler, which offers i18n support without any configurations.

```ts
import { source } from '@/lib/source';
import { createFromSource } from 'fumadocs-core/search/server';

export const { GET } = createFromSource(source);
```

In favour of this, the new search client of Fumadocs is introduced with support for different API clients.
This includes Algolia, Orama (static and dynamic with route handlers).

```ts
import { useDocsSearch } from 'fumadocs-core/search/client';

const client = useDocsSearch({
  type: 'static',
});
```

See [Search API](/docs/headless/search).

### Static Search

For sites with static export, you cannot use route handlers.
We now support client-side search using search indexes generated during build time.

See [Static Search](/docs/headless/search/orama#static-export).

### Less Dependencies

I'm always working to reduce the dependencies required for Fumadocs, that is one reason why we separated Fumadocs into different packages.

Fumadocs UI now bundles icons from `lucide-react`, for Next.js apps that is not using Lucide, they can avoid downloading the entire icon library.

And `swr` is no longer used for search client, we implemented a light `useQuery` hook with extra care on React performance optimization.

### New Metadata Image API

To improve code organization, we made a Metadata Image API on Fumadocs Core.
It is a tiny wrapper over Next.js Metadata API, composes seamlessly with Source API.

```ts title="lib/metadata.ts"
import { createMetadataImage } from 'fumadocs-core/server';
import { source } from '@/lib/source';

export const metadataImage = createMetadataImage({
  imageRoute: '/docs-og',
  source,
});
```

```ts title="route.ts"
import { generateOGImage } from 'fumadocs-ui/og';
import { metadataImage } from '@/lib/metadata';

export const GET = metadataImage.createAPI((page) => {
  return generateOGImage({
    title: page.data.title,
    description: page.data.description,
    site: 'My App',
  });
});

export function generateStaticParams() {
  return metadataImage.generateParams();
}
```

```tsx title="page.tsx"
import { source } from '@/lib/source';
import { metadataImage } from '@/lib/metadata';
import { notFound } from 'next/navigation';

export function generateMetadata({ params }: { params: { slug?: string[] } }) {
  const page = source.getPage(params.slug);
  if (!page) notFound();

  return metadataImage.withImage(page.slugs, {
    title: page.data.title,
    description: page.data.description,
  });
}
```

In favour of this, the `getImageMeta` function from `fumadocs-ui/og` has been removed.

### Shorthands

As you may notice, we introduced more abstractions to reduce the setup steps required for enabling some features.
It is also required for the code generator from Fumadocs CLI to work.

Like the `generateParams` function, it enables zero-configuration i18n support for Next.js `generateStaticParams`.

```ts
import { source } from '@/lib/source';

export function generateStaticParams() {
  return source.generateParams();
}
```

### Better Card Component

Fumadocs UI Card can now support usage without `href`.
You can pass children as React node, Typography styles will be applied correctly.

```mdx
<Card icon={<Database />} title='Content Source'>

The input/source of your content, it can be a CMS, or local data layers like [Content Collections](https://www.content-collections.dev) and [Fumadocs MDX](/docs/mdx).

</Card>
```

### Better Category Component

The original `DocsCategory` component was copied from our official docs, which is a very simple implementation that doesn't take page tree into account.

Now it accepts the source object via `from` prop.

```tsx title="page.tsx"
import { source } from '@/lib/source';
import { DocsCategory } from 'fumadocs-ui/page';

const page = source.getPage(params.slug);

<DocsCategory page={page} from={source} />;
```

By default, it takes the `locale` property from `page` to find the corresponding page tree to traverse.
You can also force a page tree.

```tsx title="page.tsx (i18n enabled)"
import { source } from '@/lib/source';
import { DocsCategory } from 'fumadocs-ui/page';

const page = source.getPage(params.slug, params.lang);

<DocsCategory page={page} from={source} tree={source.pageTree['en']} />;
```

### OpenAPI Tag Display Name

Change the display name with `x-displayName`.

```yaml title="openapi.yaml"
tags:
  - name: test
    description: this is a tag.
    x-displayName: My Test Name
```

### Better TypeScript Docs Automation

The `AutoTypeTable` component now supports a `type` prop, you can use TypeScript inside the field:

```mdx
<AutoTypeTable
  path="file.ts"
  name="B"
  type={`
import { ReactNode } from "react"
export type B = ReactNode | { world: string }
`}
/>
```

And code highlighting in typedoc is also supported with Shiki.

We **highly recommend** to use `createTypeTable` instead of importing the component in MDX files, this allows a single instance of TypeScript Compiler API to be shared.
See [Auto Type Table](/docs/ui/components/auto-type-table).

### Next.js 15

Fumadocs v14 is compatible with Next.js 15, supporting sync and async usages of dynamic APIs.

<Callout type="info" title="Backward compatible">
  Next.js 14 is also supported, notice that guides/tutorials in the docs are
  mainly for Next.js 15.
</Callout>

## UI Improvements

### Navbar Links

The navigation menu on Home layout is redesigned, with better animation and flexibility.

See the [new API](/docs/ui/navigation).

![New Navbar](/blog/v14-navbar.png)

### Link Styles

You can escape Tailwind CSS Typography styles for the `a` tag with `data-card` attribute.

```jsx
<a data-card="">
  No styles applied <code>But it does</code>
</a>
```

### Disable Theme Switch

You can disable the default theme switcher with `disableThemeSwitch` on layouts.

## Breaking Changes

### Move `dir` option from `defineDocs`

```ts
import { defineDocs } from 'fumadocs-mdx/config';

export const { docs, meta } = defineDocs({
  dir: 'my/content/dir', // define once
});
```

### Refactor Imports

**Previous**

```ts
import { DocsLayout } from 'fumadocs-ui/layout';
import { HomeLayout } from 'fumadocs-ui/home-layout';
import { HomeLayoutProps } from 'fumadocs-ui/home-layout';
```

**New Import Path**

```ts
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import { HomeLayout } from 'fumadocs-ui/layouts/home';
import { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';
```

### Twoslash UI

We moved Twoslash UI components to `fumadocs-twoslash`.
This isolates some logic from Fumadocs UI, allowing a better code organization.

Import the CSS styles and `Popup` component differently.

```ts
import 'fumadocs-twoslash/twoslash.css';

import { Popup } from 'fumadocs-twoslash/ui';
```

<Callout>It requires Tailwind CSS.</Callout>

### Remove Deprecated APIs

The previous `createI18nSearchAPIExperimental` is now renamed to `createI18nSearchAPI`.
It takes the i18n config instead of scattering the options everywhere.

The types from `fumadocs-core/search/shared` is moved to `fumadocs-core/server`.
`````

## File: apps/docs/content/blog/v15-2.mdx
`````
---
title: Fumadocs v15.2
description: From Next.js only to Next.js first.
date: 2025-03-28
author: Fuma Nama
---

## Overview

Fumadocs 15.2 introduces a layer over `fumadocs-core` to extend support to other React frameworks, including React Router and Tanstack Start. Other frameworks can also be supported using the `FrameworkProvider` from `fumadocs-core/framework/base`.

### Why?

The main focus of Fumadocs is flexibility, I aim to support more frameworks as long as it doesn't change the fundamentals of Fumadocs, like the separation of core and UI package.

The React.js ecosystem is a joy to work with, porting Fumadocs to other frameworks isn't as difficult as I thought.
It's also my goal to make it work not only for Next.js devs, but also everyone in the ecosystem who is using a SSR-compatible React framework.

### Breaking Changes

This is a minor release, it shouldn't break any previous usages unless you're relying on the lower level APIs from `fumadocs-core` without `fumadocs-ui`.

Fumadocs Core now requires a `FrameworkProvider`. It's as simple as wrapping it with appropriate provider:

```tsx
import { NextProvider } from 'fumadocs-core/framework/next';

export function Provider({ children }) {
  return <NextProvider>{children}</NextProvider>;
}
```

If you're using Fumadocs UI, there's no need to change. `RootProvider` included it by default, and allows you to provide your own framework with:

```tsx
import { RootProvider } from 'fumadocs-ui/provider/base';

export function Provider({ children }) {
  // now it doesn't add the Next.js provider
  return <RootProvider>{children}</RootProvider>;
}
```

Please report issues if you find any public APIs are broken unexpectedly.

### Compilation Time

15.2 also included some small performance improvements to Fumadocs, the time taken for Turbopack to start dev server and compile its first docs page is about 2-3 seconds.

This change also potentially allows Fumadocs to run on Vite, production build of minimal React Router setup only takes around 4s on a Macbook.

## Try it out

Upgrade from your existing Next.js docs:

```bash
pnpm update -i -r
```

If you want to try the React Router example:

```bash
pnpm create fumadocs-app
```

### Future Plans

15.2 doesn't support Astro, and probably won't unless better React.js support is provided by Astro.

- `transition:persist` is needed for Fumadocs UI layouts, however this will also affect its children (e.g. MDX content), causing page content to be persisted even after navigation.
- React contexts cannot work across islands, this changes the usage of Fumadocs significantly and hence require a redesign of APIs.

Fumadocs will continue to be Next.js first, the docs won't be changed to generalize usages of other frameworks. Instead, a new docs site will be developed for other frameworks (planned).
`````

## File: apps/docs/content/blog/v15.mdx
`````
---
title: Fumadocs v15
description: Tailwind CSS v4
author: Fuma Nama
date: 2025-01-24
---

## Overview

The purpose of v15 is mainly to support Tailwind CSS v4.
Tailwind CSS v4 is a complete redesign of its API and internals, to fully adhere to the new CSS-first config style, a breaking change is required.

Fumadocs v15 has no other significant changes other than migrating the config to Tailwind CSS v4.

## Breaking Changes

Before making the switch, upgrade your site to Tailwind CSS v4 following their [upgrade guide](https://tailwindcss.com/docs/upgrade-guide).
You can remove the unused `tailwind.config.js` file and fully rely on the new CSS-first config.

Add `@import` to the presets exported by Fumadocs UI, and include the `fumadocs-ui` package in the source.

```css title="Tailwind CSS"
@import 'tailwindcss';
@import 'fumadocs-ui/css/neutral.css';
@import 'fumadocs-ui/css/preset.css';

/* relative to the CSS file, make sure it's correct for your app */
@source '../node_modules/fumadocs-ui/dist/**/*.js';
```

Since v15, you will no longer pass options in JavaScript to customise plugins.
Instead, you can use the new alternatives in Tailwind CSS v4.

### `addGlobalColors: true`

Forward the colors again:

```css
@theme {
  --color-primary: var(--color-fd-primary);
  /* same for other colors */
}
```

### CSS Variables

Fumadocs no longer use `--fd-<color>` like `--fd-primary: 0 0% 0%` for colors, it directly defines and uses colors in `@theme`.
Instead of the previous format, it uses `hsl()`:

```css
@theme {
  --color-fd-primary: hsl(0, 0%, 100%);
}
```

### Steps

Previous Tailwind CSS utilities like `steps` & `step` are renamed to `fd-steps` and `fd-step` to avoid conflicts.

### Typography

Typography utilities including `prose`, `prose-*` modifiers will continue to work. Please report problems if they are no longer working or have unexpected change in behaviours.

## Improvements

v15 also includes some minor improvements to the UI and OpenAPI integration.

### Code Block Tabs

In the past, you needed to write the `<Tabs />` manually when separating code blocks into tabs.

````mdx
<Tabs items={["Tab 1", "Tab 2"]}>

```ts tab="Tab 1"
console.log('Hello World');
```

```ts tab="Tab 2"
console.log('Hello World');
```

</Tabs>
````

Now you can do:

````mdx
```ts tab="Tab 1"
console.log('Hello World');
```

```ts tab="Tab 2"
console.log('Hello World');
```
````

Note that the previous usage still works for those who want to customise or pass props to the `<Tabs />` component.

### Reversed Items in `meta.json`

The rest item `...` in the `pages` property of `meta.json` now supports reversed order:

```json
{
  "pages": ["z...a"]
}
```

### OpenAPI Playground

v15 improves the playground UI (inspired by the minimalism of Scalar), and brought Scalar API Client support to Fumadocs OpenAPI.

You can enable the Scalar API Client using `useScalar` option in `createOpenAPI()`:

```ts
import { createOpenAPI } from 'fumadocs-openapi/server';
import { APIPlayground } from 'fumadocs-openapi/scalar';

export const openapi = createOpenAPI({
  renderer: {
    APIPlayground,
  },
});
```

And install & configure their `@scalar/api-client-react`:

```package-install
@scalar/api-client-react
```

```css title="global.css"
@import '@scalar/api-client-react/style.css' layer(base);
```

<Callout>
  Be careful that you must configure Tailwind CSS first, using the pre-built
  stylesheet of Fumadocs UI will conflict with their `style.css` because both
  libraries use Tailwind CSS for styling.
</Callout>

## Future Plans

This update should be a simple migration for most developers updating to Tailwind CSS v4.

In the future, we also want to make further improvements to Fumadocs MDX:

- remove `transform` API - you can easily do the same with `.map()` on runtime like:

```ts
import { blog } from "@/.source"

export const updatedBlog = blog.map(...)
```

- remove Manifest API - it was designed to export search indexes, but now it's recommended to implement using route handlers.

- Mention more about our [MDX Remote](/docs/headless/custom-source#mdx-remote) package, it will be the primary solution to handle large docs sites with performance needs that bundlers couldn't do, including lazy compilation of MDX files.
`````

## File: apps/docs/content/blog/why-docs.mdx
`````
---
title: Why do you need docs?
description: You've read so many docs, but are they necessary?
date: 2024-05-26
author: Fuma Nama
---

People often ask me, do we really need a framework to build docs sites? Well, **You don't**.

Documentation sites are so important in software development,
internal docs for developers in your company to understand the architecture,
docs for frameworks,
docs for web standards...

Building docs seems simple, but can be difficult.

There are so many paradigms to build docs, but writing beginner-friendly docs could be difficult.
As a result, people tend to use powerful docs frameworks, making the docs site interactive and straightforward.

## Over-Engineered

For the docs of a small library/API service, you probably don't need to setup a Next.js site and spend time writing your site.
Neither Nextra nor Fumadocs could be better than GitHub wiki and Swagger docs in this case.

They offer a good, decent UI, basic functionalities, and a proper workflow of authoring docs.
The DX is good enough, I can't think of a reason to switch to a full-powered docs framework just to make your docs look fancy.

I'll just recommend writing your docs in markdown, make it accessible on your GitHub repository.

## Why Framework?

Now you may wonder, why major services and frameworks have their own docs sites built with docs frameworks?

Of course, _Usually_ using things like GitHub Wiki is adequate, but it is not always true.
Let's take Component Library for example, you cannot showcase your components with Markdown.
You will constantly find an ordinary Markdown document lacks capability and flexibility.

Documentation frameworks aim to solve this problem, with the ability to integrate with major libraries like **React.js** and **Vue.js**.
Good examples are Vitepress, Mintlify and Nextra - They made writing docs more convenient and effective, while offering a better, dedicated experience to readers.

For anything more than a simple library or API service, **it is worth trying.**

### Reinvent the Wheels

I would never recommend building a "custom docs site" on your own, without a proper docs framework.
Despite the **Don't re-invent the wheels** principle, your hand-made docs site actually takes way more effort to make it decent.

1. Document Search
2. A user-friendly navigation experience
3. Reading experience
4. UI/UX Design

Implementing them properly already sounds nerve-racking, right?

The docs itself, is definitely not your first priority. You should never spend your precious time re-inventing the wheels - **it isn't worth it**.

From my perspective, I'd rather use GitHub Wiki than re-inventing the wheels.
Why don't pick a decent solution? It saves your indispensable time, and help reduce the shitty docs sites on the internet.

## What do we focus at Fumadocs?

I personally value reading experience more than a fancy eye-catching UI.
You may notice, we do not have animations everywhere, and we avoided many fancy designs.

Fanciness of UI should stay only in landing page, a docs site should focus on **content.**
Navigation elements are helpers to browse your site, never should they take up too much space on the screen.

One thing I hated the most is the design of _two sidebars_, it is confusing and meaningless.
You can just organize all items to a single, clean sidebar, but people instead added two hamburger buttons to the navbar.

<div className='mx-auto max-w-[400px]'>

![Next.js Docs](/blog/img.png)

</div>

My favourite docs site is still [Linear docs](https://linear.app/docs), looks good and simple.

## Conclusion

1. You don't need a full-powered docs framework for a small library
2. Don't make a docs site on your own, use a proper docs framework
3. Fumadocs focuses on reading experience
4. You should focus on content, too
`````

## File: apps/docs/content/docs/cli/index.mdx
`````
---
title: User Guide
description: The CLI tool that automates setups and installs components.
---

## Installation

Initialize a config for CLI:

```package-install
npx @fumadocs/cli
```

You can change the output paths of components in the config.

### Components

Select and install components.

```package-install
npx @fumadocs/cli add
```

You can pass component names directly.

```package-install
npx @fumadocs/cli add banner files
```

#### How the magic works?

The CLI fetches the latest version of component from the GitHub repository of Fumadocs.
When you install a component, it is guaranteed to be up-to-date.

In addition, it also transforms import paths.
Make sure to use the latest version of CLI

> This is highly inspired by Shadcn UI.

### Customise

A simple way to customise Fumadocs layouts.

```package-install
npx @fumadocs/cli customise
```

### Tree

Generate files tree for Fumadocs UI `Files` component, using the `tree` command from your terminal.

```package-install
npx @fumadocs/cli tree ./my-dir ./output.tsx
```

You can output MDX files too:

```package-install
npx @fumadocs/cli tree ./my-dir ./output.mdx
```

See help for further details:

```package-install
npx @fumadocs/cli tree -h
```

#### Example Output

```tsx title="output.tsx"
import { File, Folder, Files } from 'fumadocs-ui/components/files';

export default (
  <Files>
    <Folder name="app">
      <File name="layout.tsx" />
      <File name="page.tsx" />
      <File name="global.css" />
    </Folder>
    <Folder name="components">
      <File name="button.tsx" />
      <File name="tabs.tsx" />
      <File name="dialog.tsx" />
    </Folder>
    <File name="package.json" />
  </Files>
);
```
`````

## File: apps/docs/content/docs/headless/components/breadcrumb.mdx
`````
---
title: Breadcrumb
description: The navigation component at the top of the screen
---

A hook for implementing Breadcrumb in your documentation. It returns breadcrumb items for a page based on the given page tree.

> If present, the index page of a folder will be used as the item.

## Usage

It exports a `useBreadcrumb` hook:

```ts twoslash
declare const tree: any;
// ---cut---
import { usePathname } from 'next/navigation';
import { useBreadcrumb } from 'fumadocs-core/breadcrumb';

const pathname = usePathname();
const items = useBreadcrumb(pathname, tree);
//    ^?
```

### Example

A styled example.

```tsx
'use client';
import { usePathname } from 'next/navigation';
import { useBreadcrumb } from 'fumadocs-core/breadcrumb';
import type { PageTree } from 'fumadocs-core/server';
import { Fragment } from 'react';
import { ChevronRight } from 'lucide-react';
import Link from 'next/link';

export function Breadcrumb({ tree }: { tree: PageTree.Root }) {
  const pathname = usePathname();
  const items = useBreadcrumb(pathname, tree);

  if (items.length === 0) return null;

  return (
    <div className="-mb-3 flex flex-row items-center gap-1 text-sm font-medium text-fd-muted-foreground">
      {items.map((item, i) => (
        <Fragment key={i}>
          {i !== 0 && (
            <ChevronRight className="size-4 shrink-0 rtl:rotate-180" />
          )}
          {item.url ? (
            <Link
              href={item.url}
              className="truncate hover:text-fd-accent-foreground"
            >
              {item.name}
            </Link>
          ) : (
            <span className="truncate">{item.name}</span>
          )}
        </Fragment>
      ))}
    </div>
  );
}
```

You can use it by passing the page tree via `tree` prop in a server component.

### Breadcrumb Item

<AutoTypeTable path="./content/docs/headless/props.ts" name="BreadcrumbItem" />
`````

## File: apps/docs/content/docs/headless/components/index.mdx
`````
---
title: Components
index: true
description: Blocks for your docs
---
`````

## File: apps/docs/content/docs/headless/components/link.mdx
`````
---
title: Link
description: A Link component that handles external links
---

A component that wraps `next/link` and automatically handles external links in the document.
When an external URL is detected, it uses `<a>` instead of the Next.js Link
Component. The `rel` property is automatically generated.

## Usage

Usage is the same as using `<a>`.

```mdx
import Link from 'fumadocs-core/link';

<Link href="/docs/components">Click Me</Link>
```

### External

You can force a URL to be external by passing an `external` prop.

### Dynamic hrefs

Dynamic hrefs are no longer supported in Next.js App Router. You can enable
dynamic hrefs by importing `dynamic-link` instead.

```mdx
import { DynamicLink } from 'fumadocs-core/dynamic-link';

<DynamicLink href="/[lang]/components">Click Me</DynamicLink>
```
`````

## File: apps/docs/content/docs/headless/components/sidebar.mdx
`````
---
title: Sidebar
description: The navigation bar at the side of the viewport
---

A sidebar component which handles device resizing and removes scroll bar
automatically.

## Usage

```tsx
import * as Base from 'fumadocs-core/sidebar';

return (
  <Base.SidebarProvider>
    <Base.SidebarTrigger />
    <Base.SidebarList />
  </Base.SidebarProvider>
);
```

### Sidebar Provider

<AutoTypeTable
  path="./content/docs/headless/props.ts"
  name="SidebarProviderProps"
/>

### Sidebar Trigger

Opens the sidebar on click.

<AutoTypeTable
  path="./content/docs/headless/props.ts"
  name="SidebarTriggerProps"
/>

### Sidebar List

| Data Attribute | Values        | Description     |
| -------------- | ------------- | --------------- |
| `data-open`    | `true, false` | Is sidebar open |

<AutoTypeTable
  path="./content/docs/headless/props.ts"
  type="SidebarContentProps"
/>
`````

## File: apps/docs/content/docs/headless/components/toc.mdx
`````
---
title: TOC
description: Table of Contents
---

A Table of Contents with active anchor observer and auto scroll.

## Usage

```tsx
import * as Base from 'fumadocs-core/toc';

return (
  <Base.AnchorProvider>
    <Base.ScrollProvider>
      <Base.TOCItem />
      <Base.TOCItem />
    </Base.ScrollProvider>
  </Base.AnchorProvider>
);
```

### Anchor Provider

Watches for the active anchor using the Intersection Observer API.

<AutoTypeTable
  path="./content/docs/headless/props.ts"
  name="AnchorProviderProps"
/>

### Scroll Provider

Scrolls the scroll container to the active anchor.

<AutoTypeTable
  path="./content/docs/headless/props.ts"
  name="ScrollProviderProps"
/>

### TOC Item

An anchor item for jumping to the target anchor.

| Data Attribute | Values        | Description          |
| -------------- | ------------- | -------------------- |
| `data-active`  | `true, false` | Is the anchor active |

## Example

<include>./toc-example.tsx</include>
`````

## File: apps/docs/content/docs/headless/content-collections/index.mdx
`````
---
title: Content Collections
description: Use Content Collections for Fumadocs
---

[Content Collections](https://www.content-collections.dev) is a library that transforms your content into type-safe data collections.

## Setup

Install the required packages.

```package-install
@fumadocs/content-collections @content-collections/core @content-collections/mdx @content-collections/next
```

After the installation, add a path alias for the generated collections to the `tsconfig.json`.

```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"],
      "content-collections": ["./.content-collections/generated"]
    }
  }
}
```

In the Next.js configuration file, apply the plugin.

```js title="next.config.mjs"
import { withContentCollections } from '@content-collections/next';

/** @type {import('next').NextConfig} */
const config = {
  reactStrictMode: true,
};

export default withContentCollections(config);
```

To integrate with Fumadocs, add the following to your `content-collections.ts`.

<include cwd meta='title="content-collections.ts"'>
  ../../examples/content-collections/content-collections.ts
</include>

And pass it to Source API.

<include cwd meta='title="lib/source.ts"'>
  ../../examples/content-collections/lib/source.ts
</include>

Done! You can access the pages and generated page tree from Source API.

```ts
import { getPage } from '@/lib/source';

const page = getPage(slugs);

// MDX output
page?.data.body;

// Table of contents
page?.data.toc;

// Structured Data, for Search API
page?.data.structuredData;
```

### MDX Options

You can customise MDX options in the `transformMDX` function.

```ts
import { defineCollection } from '@content-collections/core';
import { transformMDX } from '@fumadocs/content-collections/configuration';

const docs = defineCollection({
  transform: (document, context) =>
    transformMDX(document, context, {
      // options here
    }),
});
```

### Import Components

To use components from other packages like Fumadocs UI, pass them to your `<MDXContent />` component.

```tsx
import { MDXContent } from '@content-collections/mdx/react';
import { getMDXComponents } from '@/mdx-components';

<MDXContent code="..." components={getMDXComponents()} />;
```

You can also import them in MDX Files, but it is not recommended.

<Callout title='Deep Dive: Why?'>
    Content Collections uses `mdx-bundler` to bundle MDX files.

    To support importing a package from node modules, Fumadocs added a default value to the `cwd` option of MDX Bundler.
    It works good, but we still **do not** recommend importing components in MDX files.

    Reasons:

    - It requires esbuild to bundle these components, while it should be done by the Next.js bundler (for features of Server Components)
    - You can refactor the import path of components without changing your MDX files.
    - With Remote Sources, it doesn't make sense to add an import in MDX files.

</Callout>
`````

## File: apps/docs/content/docs/headless/mdx/headings.mdx
`````
---
title: Headings
description: Process headings from your document
---

## Remark Heading

Applies ids to headings.

```ts title="MDX Compiler"
import { compile } from '@mdx-js/mdx';
import { remarkHeading } from 'fumadocs-core/mdx-plugins';

await compile('...', {
  remarkPlugins: [remarkHeading],
});
```

> This plugin is included by default on Fumadocs MDX.

### Extract TOC

By default, it extracts the headings (table of contents) of a document to `vfile.data.toc`.
You can disable it with:

```ts
import { remarkHeading } from 'fumadocs-core/mdx-plugins';

export default {
  remarkPlugins: [[remarkHeading, { generateToc: false }]],
};
```

### Custom Ids [#custom-heading-id]

You can customise the heading id with `[#slug]`.

```md
# heading [#slug]
```

### Output

An array of `TOCItemType`.

<AutoTypeTable path="./content/docs/headless/props.ts" name="TOCItemType" />

## Rehype TOC

Exports table of contents (an array of `TOCItemType`), it allows JSX nodes which is not possible with a Remark plugin.

> It requires MDX.js.

### Usage

```ts
import { rehypeToc } from 'fumadocs-core/mdx-plugins';

export default {
  rehypePlugins: [rehypeToc],
};
```

### Output

For a Markdown document:

```md
## Hello `code`
```

An export will be created:

```jsx
export const toc = [
  {
    title: (
      <>
        Hello <code>code</code>
      </>
    ),
    depth: 2,
    url: '#hello-code',
  },
];
```
`````

## File: apps/docs/content/docs/headless/mdx/index.mdx
`````
---
title: MDX Plugins
index: true
description: Useful remark & rehype plugins for your docs.
---
`````

## File: apps/docs/content/docs/headless/mdx/install.mdx
`````
---
title: Package Install
description: Generate code blocks for installing packages
---

<Callout type="warn" title='Deprecated'>
    For Fumadocs MDX, it is now enabled by default.

    You can use the `remarkNpm` plugin from `fumadocs-core/mdx-plugins` instead.

</Callout>

## Usage

```package-install
fumadocs-docgen
```

Add the remark plugin.

```ts title="source.config.ts" tab="Fumadocs MDX"
import { remarkInstall } from 'fumadocs-docgen';
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    remarkPlugins: [remarkInstall],
  },
});
```

```ts tab="MDX Compiler"
import { compile } from '@mdx-js/mdx';
import { remarkInstall } from 'fumadocs-docgen';

await compile('...', {
  remarkPlugins: [remarkInstall],
});
```

Define the required components.

```tsx title="mdx-components.tsx (Fumadocs UI)"
import { Tab, Tabs } from 'fumadocs-ui/components/tabs';
import defaultComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultComponents,
    Tab,
    Tabs,
    ...components,
  };
}
```

| Component |                                    |
| --------- | ---------------------------------- |
| Tabs      | Accepts an array of item (`items`) |
| Tab       | Accepts the name of item (`value`) |

Create code blocks with `package-install` as language.

````mdx
```package-install
my-package
```

```package-install
npm i my-package -D
```
````

### Output

The following structure should be generated by the plugin.

```mdx
<Tabs items={['npm', 'pnpm', 'yarn', 'bun']}>
  <Tab value="npm">...</Tab>
  <Tab value="pnpm">...</Tab>
  <Tab value="yarn">...</Tab>
  <Tab value="bun">...</Tab>
</Tabs>
```

```package-install
my-package
```

## Options

### Persistent

When using with Fumadocs UI, you can enable persistence with the `persist` option.

```ts title="source.config.ts" tab="Fumadocs MDX"
import { remarkInstall } from 'fumadocs-docgen';
import { defineConfig } from 'fumadocs-mdx/config';

const remarkInstallOptions = {
  persist: {
    id: 'some-id',
  },
};

export default defineConfig({
  mdxOptions: {
    remarkPlugins: [[remarkInstall, remarkInstallOptions]],
  },
});
```

```ts tab="MDX Compiler"
import { compile } from '@mdx-js/mdx';
import { remarkInstall } from 'fumadocs-docgen';

const remarkInstallOptions = {
  persist: {
    id: 'some-id',
  },
};

await compile('...', {
  remarkPlugins: [[remarkInstall, remarkInstallOptions]],
});
```

This will instead generate:

```mdx
<Tabs groupId="some-id" persist items={[...]}>
  ...
</Tabs>
```
`````

## File: apps/docs/content/docs/headless/mdx/rehype-code.mdx
`````
---
title: Rehype Code
description: Code syntax highlighter
---

A wrapper of [Shiki](https://shiki.style), the built-in syntax highlighter.

## Usage

Add the rehype plugin.

```ts title="MDX Compiler"
import { compile } from '@mdx-js/mdx';
import { rehypeCode } from 'fumadocs-core/mdx-plugins';

await compile('...', {
  rehypePlugins: [rehypeCode],
});
```

> This plugin is included by default on Fumadocs MDX.

### Output

A codeblock wrapped in `<pre />` element.

```html
<pre>
<code>...</code>
</pre>
```

### Meta

It parses the `title` meta string, and adds it to the `pre` element as an attribute.

````mdx
```js title="Title"
console.log('Hello');
```
````

You may filter the meta string before processing it with the `filterMetaString` option.

### Inline Code

`console.log("hello world"){:js}` works.

See https://shiki.style/packages/rehype#inline-code.

### Icon

Adds an icon according to the language of the codeblock.
It outputs HTML, you might need to render it with React `dangerouslySetInnerHTML`.

```jsx
<pre icon="<svg />">...</pre>
```

Disable or customise icons with the `icon` option.

### More Options

See [Shiki](https://shiki.style).
`````

## File: apps/docs/content/docs/headless/mdx/remark-admonition.mdx
`````
---
title: Remark Admonition
description: Use Admonition in Fumadocs
---

In Docusaurus, there's an [Admonition syntax](https://docusaurus.io/docs/markdown-features/admonitions).

For people migrating from Docusaurus, you can enable this remark plugin to support the Admonition syntax.

## Usage

```ts title="source.config.ts" tab="Fumadocs MDX"
import { remarkAdmonition } from 'fumadocs-core/mdx-plugins';
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    remarkPlugins: [remarkAdmonition],
  },
});
```

```ts tab="MDX Compiler"
import { compile } from '@mdx-js/mdx';
import { remarkAdmonition } from 'fumadocs-core/mdx-plugins';

await compile('...', {
  remarkPlugins: [remarkAdmonition],
});
```

### Input

```md
:::warning
Hello World
:::
```

### Output

```mdx
<Callout type='warn'>

Hello World

</Callout>
```

### When to use

We highly recommend using the JSX syntax of MDX instead.
It's more flexible, some editors support IntelliSense in MDX files.

```mdx
<Callout type='warn'>

Hello World

</Callout>
```
`````

## File: apps/docs/content/docs/headless/mdx/remark-image.mdx
`````
---
title: Remark Image
description: Make images compatible with Next.js Image Optimization
---

## Usage

Add it to your Remark plugins.

```ts title="MDX Compiler"
import { compile } from '@mdx-js/mdx';
import { remarkImage } from 'fumadocs-core/mdx-plugins';

await compile('...', {
  remarkPlugins: [remarkImage],
});
```

> This plugin is included by default on Fumadocs MDX.

Supported:

- Local Images
- External URLs
- Next.js static imports

### How It Works

It transforms your `![image](/test.png)` into Next.js Image usage, and add required props like `width` and `height`.

By default, it uses **static imports** to import local images, which supports the `placeholder` option of Next.js Image.
Next.js can handle image imports with its built-in image loader.

Otherwise, it uses the file system or an HTTP request to download the image and obtain its size.

### Options

<AutoTypeTable
  path="./content/docs/headless/props.ts"
  name="RemarkImageOptions"
/>

### Example: With Imports

```mdx
![Hello](/hello.png)
![Test](https://example.com/image.png)
```

Yields:

```mdx
import HelloImage from './public/hello.png';

<img alt="Hello" src={HelloImage} />
<img
  alt="Test"
  src="https://example.com/image.png"
  width="1980"
  height="1080"
/>
```

Where `./public/hello.png` points to the image in public directory.

### Example: Without Imports

You can disable Next.js static imports on local images.

```ts
import { remarkImage } from 'fumadocs-core/mdx-plugins';

export default {
  remarkPlugins: [[remarkImage, { useImport: false }]],
};
```

```mdx
![Hello](/hello.png)
![Test](https://example.com/image.png)
```

Yields:

```mdx
<img alt="Hello" src="/hello.png" width="1980" height="1080" />
<img
  alt="Test"
  src="https://example.com/image.png"
  width="1980"
  height="1080"
/>
```

### Example: Relative Paths

When `useImport` is enabled, you can reference local images using relative paths.

```mdx
![Hello](./hello.png)
```

Be careful that using it with `useImport` disabled **doesn't work**.
Next.js will not add the image to public assets unless you have imported it in code.
For images in public directory, you can just reference them without relative paths.

### Example: Public Directory

Customise the path of public directory

```ts
import { remarkImage } from 'fumadocs-core/mdx-plugins';
import path from 'node:path';

export default {
  remarkPlugins: [
    remarkImage,
    {
      publicDir: path.join(process.cwd(), 'dir'),
    },
  ],
};
```

You can pass a URL too.

```ts
import { remarkImage } from 'fumadocs-core/mdx-plugins';

export default {
  remarkPlugins: [
    remarkImage,
    {
      publicDir: 'http://localhost:3000/images',
    },
  ],
};
```
`````

## File: apps/docs/content/docs/headless/mdx/remark-ts2js.mdx
`````
---
title: Remark TS to JS
description: A remark plugin to transform TypeScript codeblocks into two tabs of codeblock with its JavaScript variant.
---

## Usage

Install dependencies:

```package-install
fumadocs-docgen oxc-transform
```

Add `oxc-transform` to `serverExternalPackages` in `next.config.mjs`:

```js title="next.config.mjs"
import { createMDX } from 'fumadocs-mdx/next';

/** @type {import('next').NextConfig} */
const config = {
  reactStrictMode: true,
  serverExternalPackages: ['oxc-transform'],
};

const withMDX = createMDX();

export default withMDX(config);
```

Add the remark plugin:

```ts title="source.config.ts" tab="Fumadocs MDX"
import { remarkTypeScriptToJavaScript } from 'fumadocs-docgen/remark-ts2js';
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    remarkPlugins: [remarkTypeScriptToJavaScript],
  },
});
```

```ts tab="MDX Compiler"
import { remarkTypeScriptToJavaScript } from 'fumadocs-docgen/remark-ts2js';
import { compile } from '@mdx-js/mdx';

await compile('...', {
  remarkPlugins: [remarkTypeScriptToJavaScript],
});
```

Finally, make sure to define the required MDX components: `Tabs` and `Tab`.

```tsx title="mdx-components.tsx (Fumadocs UI)"
import { Tab, Tabs } from 'fumadocs-ui/components/tabs';
import defaultComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultComponents,
    Tab,
    Tabs,
    ...components,
  };
}
```

You can now enable it on TypeScript/TSX codeblocks, like:

````md
```tsx ts2js
import { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return <div>{children}</div>;
}
```
````

```tsx ts2js
import { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return <div>{children}</div>;
}
```
`````

## File: apps/docs/content/docs/headless/mdx/structure.mdx
`````
---
title: Remark Structure
description: Extract information from your documents, useful for implementing document search
---

## Usage

Add it as a remark plugin.

```ts title="MDX Compiler"
import { compile } from '@mdx-js/mdx';
import { remarkStructure } from 'fumadocs-core/mdx-plugins';

const vfile = await compile('...', {
  remarkPlugins: [remarkStructure],
});
```

> This plugin is included by default on Fumadocs MDX.

Extracted information could be found in `vfile.data.structuredData`, you may
write your own plugin to convert it into a MDX export.

### Options

<AutoTypeTable
  path="./content/docs/headless/props.ts"
  name="StructureOptions"
/>

### Output

A list of headings and contents. Paragraphs will be extracted to the `contents`
array, each item contains a `heading` prop indicating the heading of paragraph.

<Callout title="Note">A heading can have multiple paragraphs.</Callout>

#### Heading

| Prop      |                                      |
| --------- | ------------------------------------ |
| `id`      | unique identifier or slug of heading |
| `content` | Text content                         |

#### Content

| Prop      |                                 |
| --------- | ------------------------------- |
| `heading` | Heading of paragraph (nullable) |
| `content` | Text content                    |

## As a Function

Accepts MDX/markdown content and return structurized data.

```ts
import { structure } from 'fumadocs-core/mdx-plugins';

structure(page.body.raw);
```

<Callout title="Tip" className="mt-4">
If you have custom remark plugins enabled, such as
`remark-math`, you have to pass these plugins to the function. This avoids unreadable content on paragraphs.

```ts
import { structure } from 'fumadocs-core/mdx-plugins';
import remarkMath from 'remark-math';

structure(page.body.raw, [remarkMath]);
```

</Callout>

### Parameters

| Parameter       |                        |
| --------------- | ---------------------- |
| `content`       | MDX/markdown content   |
| `remarkPlugins` | List of remark plugins |
| `options`       | Custom options         |
`````

## File: apps/docs/content/docs/headless/search/algolia.mdx
`````
---
title: Algolia Search
description: Integrate Algolia Search with Fumadocs
---

<Callout title="Notice">
  If you're using Algolia's free tier, you have to [display their logo on your
  search dialog](https://algolia.com/policies/free-services-terms).
</Callout>

## Introduction

The Algolia Integration automatically configures Algolia Search for document search.

It creates a record for **each paragraph** in your document, it is also recommended by Algolia.

Each record contains searchable attributes:

| Attribute | Description           |
| --------- | --------------------- |
| `title`   | Page Title            |
| `section` | Heading ID (nullable) |
| `content` | Paragraph content     |

The `section` field only exists in paragraphs under a heading. Headings and
paragraphs are indexed as an individual record, grouped by their page ID.

Notice that it expects the `url` property of a page to be unique, you shouldn't have two pages with the same
url.

## Setup

Install dependencies:

```package-install
algoliasearch
```

### Sign up on Algolia

Sign up and obtain the app id and API keys for your search. Store these
credentials in environment variables.

### Sync Search Indexes

Export the search indexes from Next.js using a route handler, this way we can access the search indexes after production build:

```ts title="app/static.json/route.ts"
import { NextResponse } from 'next/server';
import { type DocumentRecord } from 'fumadocs-core/search/algolia';
import { source } from '@/lib/source';

export const revalidate = false;

export function GET() {
  const results: DocumentRecord[] = [];

  for (const page of source.getPages()) {
    results.push({
      _id: page.url,
      structured: page.data.structuredData,
      url: page.url,
      title: page.data.title,
      description: page.data.description,
    });
  }

  return NextResponse.json(results);
}
```

Make a script to sync search indexes:

<include lang="js" meta='title="update-index.mjs"'>
  ./sync-algolia.mjs
</include>

The `sync` function will update the index settings and sync search indexes.

Now run the script after build:

```json title="package.json"
{
  "scripts": {
    "build": "next build && node ./update-index.mjs"
  }
}
```

### Workflow

You may make it a script and manually sync with `node ./update-index.mjs`, or
integrate it with your CI/CD pipeline.

<Callout type="warn" title="Typescript Usage">
  If you are running the script with [TSX](https://github.com/privatenumber/tsx)
  or other similar Typescript executors, ensure to name it `.mts` for best ESM
  compatibility.
</Callout>

### Search UI

You can consider different options for implementing the UI:

- Using [Fumadocs UI search dialog](/docs/ui/search/algolia).
- Build your own using the built-in search client hook:

  ```ts twoslash
  import { liteClient } from 'algoliasearch/lite';
  import { useDocsSearch } from 'fumadocs-core/search/client';

  const client = liteClient('id', 'key');

  const { search, setSearch, query } = useDocsSearch({
    type: 'algolia',
    indexName: 'document',
    client,
  });
  ```

- Use their official clients directly.

## Options

### Tag Filter

To configure tag filtering, add a `tag` value to indexes.

```js
import { sync } from 'fumadocs-core/search/algolia';

void sync(client, {
  indexName: 'document',
  documents: records.map((index) => ({
    ...index,
    tag: 'value', // [!code ++]
  })),
});
```

And update your search client:

- **Fumadocs UI**: Enable [Tag Filter](/docs/ui/search/algolia#tag-filter) on Search UI.
- **Search Client**: You can add the tag filter like:

  ```ts
  import { useDocsSearch } from 'fumadocs-core/search/client';

  const { search, setSearch, query } = useDocsSearch({
    tag: '<your tag value>',
    // ...
  });
  ```

The `tag` field is an attribute for faceting. You can also use the filter `tag:value` on Algolia search clients.
`````

## File: apps/docs/content/docs/headless/search/index.mdx
`````
---
title: Search
description: Configure Search in Fumadocs
icon: Search
index: true
---
`````

## File: apps/docs/content/docs/headless/search/mixedbread.mdx
`````
---
title: Mixedbread
description: Integrate Mixedbread Search with Fumadocs
---

## Introduction

The Mixedbread Integration uses vector search to provide semantic search capabilities for your documentation. It indexes your documentation content into a vector store, enabling users to search using natural language queries and find relevant content based on meaning rather than just keyword matching.

## Setup

### Get your API Key

1. Sign up at [Mixedbread](https://platform.mixedbread.com)
2. Navigate to [API Keys](https://platform.mixedbread.com/platform?next=api-keys)
3. Create a new API key and store it in your environment variables

### Create a Vector Store

To sync your documentation, you'll need to create a vector store:

1. Go to the [Vector Stores](https://platform.mixedbread.com/platform?next=vector-stores) in your Mixedbread dashboard
2. Create a new vector store for your documentation
3. Copy the vector store ID

### Sync Documentation

Use the [Mixedbread CLI](https://www.mixedbread.com/cli) to sync your documentation:

Install the CLI:

```package-install
@mixedbread/cli -D
```

Configure authentication and sync your documentation:

```bash
# Configure authentication
mxbai config keys add YOUR_API_KEY

# Sync your documentation
mxbai vs sync YOUR_VECTOR_STORE_ID "./content/docs"
```

The CLI will automatically detect changes in your documentation and update the vector store accordingly.

### Workflow

You can automatically sync your documentation by adding a sync script to your `package.json`:

```json
{
  "scripts": {
    "build": "next build && npm run sync-content",
    "sync-content": "mxbai vs sync YOUR_VECTOR_STORE_ID './content/docs' --ci"
  }
}
```

## Options

### Tag Filter

To filter search results by tags, add a tag field to your document metadata:

```typescript
---
title: Mixedbread
description: Integrate Mixedbread Search with Fumadocs
url: /docs/headless/search/mixedbread
// [!code ++]
tag: docs
---
...
```

And update your search client:

- **Fumadocs UI**: Enable [Tag Filter](/docs/ui/search/orama#tag-filter) on Search UI.
- **Search Client**: You can add the tag filter like:

  ```ts
  import { useDocsSearch } from 'fumadocs-core/search/client';

  const { search, setSearch, query } = useDocsSearch({
    tag: '<your tag value>',
    // ...
  });
  ```

This allows you to scope searches to specific sections of your documentation.
`````

## File: apps/docs/content/docs/headless/search/orama-cloud.mdx
`````
---
title: Orama Cloud
description: Integrate with Orama Cloud
---

To begin, create an account on Orama Cloud.

## REST API

REST API integration requires your docs to upload the indexes.

1. Create a new REST API index from Dashboard.
2. Use the following schema:

   ```json
   {
     "id": "string",
     "title": "string",
     "url": "string",
     "tag": "string",
     "page_id": "string",
     "section": "string",
     "section_id": "string",
     "content": "string"
   }
   ```

3. Then, using the private API key and index ID from dashboard, create a script to sync search indexes.

   <include cwd meta='title="sync-index.mjs"' lang="js">
     ../../examples/next-mdx/scripts/sync-orama-cloud.mjs
   </include>

4. Create a route handler in your Next.js app to export search indexes.

   <include cwd meta='title="app/static.json/route.ts"'>
     ../../examples/next-mdx/app/static.json/orama-cloud.ts
   </include>

5. Run the script after `next build`.

### Search Client

To search documents on the client side, consider:

- Using [Fumadocs UI search dialog](/docs/ui/search/orama-cloud).
- Custom search UI using the built-in hook of Fumadocs:

  ```ts
  import { useDocsSearch } from 'fumadocs-core/search/client';
  import { OramaClient } from '@oramacloud/client';

  const client = new OramaClient();

  const { search, setSearch, query } = useDocsSearch({
    type: 'orama-cloud',
    client,
    params: {
      // search params
    },
  });
  ```

- Use their search client directly.

## Web Crawler

1. Create a Crawler index from dashboard, and configure it correctly with the "Documentation" preset.
2. Copy the public API key and index ID from dashboard

### Search Client

Same as REST API integration, but make sure to set `index` to `crawler`.

```ts
import { useDocsSearch } from 'fumadocs-core/search/client';
import { OramaClient } from '@oramacloud/client';

const client = new OramaClient({
  endpoint: '<endpoint_url>',
  api_key: '<api_key>',
});

const { search, setSearch, query } = useDocsSearch({
  type: 'orama-cloud',
  index: 'crawler',
  client,
  params: {
    // optional search params
  },
});
```

It's same for Fumadocs UI.
`````

## File: apps/docs/content/docs/headless/search/orama.mdx
`````
---
title: Built-in Search
description: Built-in document search of Fumadocs
---

Fumadocs supports document search with Orama, It is the default but also the recommended option since it can be self-hosted and totally free.

## Setup

Host the server for handling search requests.

<Tabs items={['From Source', 'From Search Indexes', 'From Search Indexes (Raw Content)']}>

<Tab>

Create a route handler from source object.

<include cwd meta='title="app/api/search/route.ts"'>
  ../../examples/next-mdx/app/api/search/route.ts
</include>

</Tab>

<Tab>

Pass search indexes to the function, each index needs a `structuredData` field.

Usually, it is provided by your content source (e.g. Fumadocs MDX). You can also extract it from Markdown/MDX document using the [Remark Structure](/docs/headless/mdx/structure) plugin.

<include cwd meta='title="app/api/search/route.ts"'>
  ../../examples/next-mdx/app/api/search/route-full.ts
</include>

</Tab>

<Tab>

Index with the raw content of document (unrecommended).

```ts title="app/api/search/route.ts"
import { allDocs } from 'content-collections';
import { createSearchAPI } from 'fumadocs-core/search/server';

export const { GET } = createSearchAPI('simple', {
  indexes: allDocs.map((docs) => ({
    title: docs.title,
    content: docs.content, // Raw Content
    url: docs.url,
  })),
});
```

</Tab>

</Tabs>

You can search documents using:

- **Fumadocs UI**: Supported out-of-the-box, see [Search UI](/docs/ui/search/orama) for details.
- **Search Client**:

```ts twoslash
import { useDocsSearch } from 'fumadocs-core/search/client';

const client = useDocsSearch({
  type: 'fetch',
});
```

<auto-type-table type='Extract<import("fumadocs-core/search/client").Client, { type: "fetch" }>' />

### Tag Filter

Support filtering results by tag, it's useful for implementing multi-docs similar to this documentation.

<include meta='title="app/api/search/route.ts"' cwd>
  ../../examples/next-mdx/app/api/search/route-tag.ts
</include>

and update your search client:

- **Fumadocs UI**: Configure [Tag Filter](/docs/ui/search/orama#tag-filter) on Search UI.
- **Search Client**: pass a tag to the hook.

```ts
import { useDocsSearch } from 'fumadocs-core/search/client';

const client = useDocsSearch({
  type: 'fetch',
  tag: '<value>', // [!code ++]
});
```

### Static Export

To work with Next.js static export, use `staticGET` from search server.

```ts title="app/api/search/route.ts"
import { source } from '@/lib/source';
import { createFromSource } from 'fumadocs-core/search/server';

// it should be cached forever
export const revalidate = false;

// [!code highlight]
export const { staticGET: GET } = createFromSource(source);
```

> `staticGET` is also available on `createSearchAPI`.

and update your search clients:

- **Fumadocs UI**: use [static client](/docs/ui/search/orama#static) on Search UI.

- **Search Client**: use `static` instead of `fetch`.

  ```ts
  import { useDocsSearch } from 'fumadocs-core/search/client';

  const client = useDocsSearch({
    type: 'static',
  });
  ```

  <AutoTypeTable type='Extract<import("fumadocs-core/search/client").Client, { type: "static" }>' />

<Callout type='warn' title="Be Careful">

    Static Search requires clients to download the exported search indexes.
    For large docs sites, it can be expensive.

    You should use cloud solutions like Orama Cloud or Algolia for these cases.

</Callout>

## Internationalization

Make sure your language is on the Orama [Supported Languages](https://docs.orama.com/open-source/supported-languages#officially-supported-languages) list.

```ts title="app/api/search/route.ts" tab="createFromSource"
import { source } from '@/lib/source';
import { createFromSource } from 'fumadocs-core/search/server';

export const { GET } = createFromSource(source, {
  localeMap: {
    // [locale]: Orama options
    ru: { language: 'russian' },
    en: { language: 'english' },
  },
});
```

<include cwd meta='title="app/api/search/route.ts" tab="createI18nSearchAPI"'>
  ../../examples/i18n/app/api/search/route-full.ts
</include>

```tsx title="components/search.tsx" tab="Static mode"
import { useDocsSearch } from 'fumadocs-core/search/client';
import { create } from '@orama/orama';

// update your `initOrama` function [!code focus:6]
function initOrama(locale?: string) {
  return create({
    schema: { _: 'string' },
    language: locale === 'ru' ? 'russian' : 'english',
  });
}

function Search() {
  const client = useDocsSearch({
    type: 'static',
    initOrama,
    locale,
    // ...
  });
}
```

For Chinese & Japanese, they require additional configurations:

```npm
@orama/tokenizers
```

<include cwd meta='title="app/api/search/route.ts" tab="createFromSource"'>
  ../../examples/i18n/app/api/search/route.ts
</include>

```tsx tab="Static mode" title="components/search.tsx"
import { useDocsSearch } from 'fumadocs-core/search/client';
import { createTokenizer } from '@orama/tokenizers/mandarin';
import { create } from '@orama/orama';

// [!code focus:8]
function initOrama(locale?: string) {
  return create({
    schema: { _: 'string' },
    components: {
      tokenizer: locale === 'cn' ? createTokenizer() : undefined,
    },
  });
}

function Search() {
  const client = useDocsSearch({
    type: 'static',
    initOrama,
  });
  // ...
}
```

and update your search clients:

- **Fumadocs UI**: No changes needed, Fumadocs UI handles this when you have i18n configured correctly.
- **Search Client**:
  Add `locale` to the search client, this will only allow pages with specified locale to be searchable by the user.

```ts
import { useDocsSearch } from 'fumadocs-core/search/client';

const { search, setSearch, query } = useDocsSearch({
  type: 'fetch',
  locale: 'cn',
});
```

## Headless

You can host the search server on other backend such as Express and Elysia.

```ts
import { initAdvancedSearch } from 'fumadocs-core/search/server';

const server = initAdvancedSearch({
  // you still have to pass indexes
});

server.search('query', {
  // you can specify `locale` and `tag` here
});
```
`````

## File: apps/docs/content/docs/headless/search/trieve.mdx
`````
---
title: Trieve Search
description: Integrate Trieve Search with Fumadocs
---

> This is a community maintained integration.

## Introduction

The Trieve Integration automatically configures Trieve Search for site search.

By default, it creates a chunk for **each paragraph** in your document, it is
officially recommended by Trieve.

## Setup

### Install Dependencies

```package-install
trieve-ts-sdk trieve-fumadocs-adapter
```

### Sign up on Trieve

Sign up and create a dataset. Then obtain 2 API keys where one has only read access and the other has admin access to create and delete chunks.
Store these credentials in environment variables.

<Callout title="Notice">
  One API Key should have only read access for the public facing search and the
  other should have admin access to create and delete chunks.
</Callout>

### Sync Dataset

You can export the search indexes from Next.js using a route handler:

```ts title="app/static.json/route.ts"
import { NextResponse } from 'next/server';
import { source } from '@/lib/source';
import { type TrieveDocument } from 'trieve-fumadocs-adapter/search/sync';

export const revalidate = false;

export function GET() {
  const results: TrieveDocument[] = [];

  for (const page of source.getPages()) {
    results.push({
      _id: page.url,
      structured: page.data.structuredData,
      url: page.url,
      title: page.data.title,
      description: page.data.description,
    });
  }

  return NextResponse.json(results);
}
```

Create a script, the `sync` function will sync search indexes.

```js title="update-index.mjs"
import * as fs from 'node:fs';
import { sync } from 'trieve-fumadocs-adapter/search/sync';
import { TrieveSDK } from 'trieve-ts-sdk';

const content = fs.readFileSync('.next/server/app/static.json.body');

// now you can pass it to `sync`
/** @type {import('trieve-fumadocs-adapter/search/sync').TrieveDocument[]} **/
const records = JSON.parse(content.toString());

const client = new TrieveSDK({
  apiKey: 'adminApiKey',
  datasetId: 'datasetId',
});

sync(client, records);
```

Make sure to run the script after build:

```json title="package.json"
{
  "scripts": {
    "build": "next build && node ./update-index.mjs"
  }
}
```

### Workflow

You may manually sync with `node ./update-index.mjs`, or
integrate it with your CI/CD pipeline.

<Callout type="info" title="Typescript Usage">
  You can use Bun or other JavaScript runtimes that supports TypeScript and ESM.
</Callout>

### Search UI

You can use their `SearchDialog` component:

```tsx title="components/search.tsx"
'use client';
import type { SharedProps } from 'fumadocs-ui/components/dialog/search';
import SearchDialog from 'trieve-fumadocs-adapter/components/dialog/search';
import { TrieveSDK } from 'trieve-ts-sdk';

const trieveClient = new TrieveSDK({
  apiKey: 'readOnlyApiKey',
  datasetId: 'datasetId',
});

export default function CustomSearchDialog(props: SharedProps) {
  return <SearchDialog trieveClient={trieveClient} {...props} />;
}
```

1. Replace `apiKey` and `datasetId` with your desired values.

2. Replace the default search dialog with your new one.

### Search Client

Add the `useTrieveSearch` hook:

```ts
import { TrieveSDK } from 'trieve-ts-sdk';
import { useTrieveSearch } from 'trieve-fumadocs-adapter/search/trieve';

const client = new TrieveSDK({
  apiKey: 'readOnlyApiKey',
  datasetId: 'datasetId',
});

const { search, setSearch, query } = useTrieveSearch(client);
```

## Options

### Tag Filter

To configure tag filtering, add a `tag` value to indexes.

```js
import { sync } from 'trieve-fumadocs-adapter/search/sync';
import { TrieveSDK } from 'trieve-ts-sdk';

const client = new TrieveSDK({
  apiKey: 'adminApiKey',
  datasetId: 'datasetId',
});

const documents = records.map((index) => ({
  ...index,
  tag: 'value', // [!code highlight]
}));

sync(client, documents);
```

#### Search UI

Enable Tag Filter.

```tsx title="components/search.tsx"
import SearchDialog from 'trieve-fumadocs-adapter/components/dialog/search';

<SearchDialog
  defaultTag="value"
  tags={[
    {
      name: 'Tag Name',
      value: 'value',
    },
  ]}
/>;
```

#### Search Client

The `tag_set` field is an attribute for filtering. To filter indexes by tag, use the filter on Trieve search clients.

```json
{
  "must": [
    {
      "field": "tag_set",
      "match": ["value"]
    }
  ]
}
```

Or with `useTrieveSearch` hook:

```ts
import { TrieveSDK } from 'trieve-ts-sdk';
import { useTrieveSearch } from 'trieve-fumadocs-adapter/search/trieve';

const client = new TrieveSDK({
  apiKey: 'readOnlyApiKey',
  datasetId: 'datasetId',
});

const { search, setSearch, query } = useTrieveSearch(
  client,
  undefined,
  '<your tag value>',
);
```
`````

## File: apps/docs/content/docs/headless/utils/find-neighbour.mdx
`````
---
title: Find Neighbours
description: Find the neighbours of a page from the page tree
---

Find the neighbours of a page from the page tree, it returns the next and
previous page of a given page. It is useful for implementing a footer.

## Usage

It requires a page tree and the url of page.

```ts
import { findNeighbour } from 'fumadocs-core/server';
import { pageTree } from '@/lib/source';

const neighbours = findNeighbour(pageTree, '/url/to/page');
```

| Parameter | Type       | Description     |
| --------- | ---------- | --------------- |
| tree      | `PageTree` | The page tree   |
| url       | `string`   | The url of page |
`````

## File: apps/docs/content/docs/headless/utils/get-toc.mdx
`````
---
title: Get TOC
description: Parse Table of contents from markdown/mdx content
---

Parse Table of contents from markdown/mdx content.

> [You can use the remark plugin directly](/docs/headless/mdx/headings)

## Usage

Note: If you're using a CMS, you should use the API provided by the CMS instead.

```ts
import { getTableOfContents } from 'fumadocs-core/server';

const toc = getTableOfContents('## markdown content');
```

### Output

An array of [`TOCItemType`](/docs/headless/mdx/headings#output) is returned.
`````

## File: apps/docs/content/docs/headless/utils/git-last-edit.mdx
`````
---
title: Last Modified Time
description: Get the last edit time of a file in Github repository
---

## Usage

Pass your repository name, and the path to file.

```ts
import { getGithubLastEdit } from 'fumadocs-core/server';

const time = await getGithubLastEdit({
  owner: 'fuma-nama',
  repo: 'fumadocs',
  // example: "content/docs/index.mdx"
  path: `content/docs/${page.path}`,
});
```

### Github Token

Notice that you may easily reach the rate limit in development mode. Hence, you
should pass a Github token for a higher rate limit.

Learn more about
[Authenticating to the REST API](https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api).

```ts
import { getGithubLastEdit } from 'fumadocs-core/server'

 const time = await getGithubLastEdit({
    ...,
    token: `Bearer ${process.env.GIT_TOKEN}`
  })
```

Also, you can skip this in development mode if you don't need that
functionality.

```ts
process.env.NODE_ENV === 'development'? null : getGithubLastEdit(...)
```
`````

## File: apps/docs/content/docs/headless/utils/index.mdx
`````
---
title: Utilities
index: true
description: Utilities to provide extra functionality to your docs
---
`````

## File: apps/docs/content/docs/headless/custom-source.mdx
`````
---
title: Custom Source
description: Build your own content source
---

## Introduction

**Fumadocs is very flexible.** You can integrate with any content source, even without an official adapter.

> This guide assumes you are experienced with Next.js App Router.

### Examples

You can see examples to use Fumadocs with a CMS, which allows a nice experience on publishing content, and real-time update without re-building the app.

- [BaseHub](https://github.com/fuma-nama/fumadocs-basehub)
- [Sanity](https://github.com/fuma-nama/fumadocs-sanity)
- [Payload CMS](https://github.com/MFarabi619/fumadocs-payloadcms)

For a custom content source implementation, you will need:

### Page Tree

You can either hardcode the page tree, or write some code to generate one.
See [Definitions of Page Tree](/docs/headless/page-tree).

Pass your Page Tree to `DocsLayout` (usually in a `layout.tsx`).

```tsx title="layout.tsx"
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout
      nav={{ title: 'Example Docs' }}
      tree={
        {
          /// your own tree
        }
      }
    >
      {children}
    </DocsLayout>
  );
}
```

The page tree is like a smarter "sidebar items", they will be referenced everywhere in the UI for navigation elements, such as the page footer.

### Docs Page

Same as a normal Next.js app, the code of your docs page is located in `[[...slug]]/page.tsx`.

#### SSG

Define the [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params) function.
It should return a list of parameters (`params`) to populate the `[[...slug]]` catch-all route.

#### Body

In the main body of page, find the corresponding page according to the slug and render its content inside the `DocsPage` component.

You also need table of contents, which can be generated with your own implementation, or using the [`getTableOfContents`](/docs/headless/utils/get-toc) utility (Markdown/MDX only).

```tsx
import { DocsPage, DocsBody } from 'fumadocs-ui/page';
import { getPage } from './my-content-source';
import { notFound } from 'next/navigation';

export default function Page({ params }: { params: { slug?: string[] } }) {
  const page = getPage(params.slug);
  if (!page) notFound();

  return (
    <DocsPage toc={page.tableOfContents}>
      <DocsBody>{page.render()}</DocsBody>
    </DocsPage>
  );
}
```

#### Metadata

Next.js offers a Metadata API for SEO, you can configure it with `generateMetadata` (similar as the code above).

### Document Search

This can be difficult considering your content may not be necessarily Markdown/MDX.
For Markdown and MDX, the built-in [Search API](/docs/headless/search/orama) is adequate for most use cases.
Otherwise, you will have to bring your own implementation.

We recommend 3rd party solutions like Algolia Search. They are more flexible than the built-in Search API, and is easier to integrate with remote sources.
Fumadocs offers a simple [Algolia Search Adapter](/docs/headless/search/algolia), which includes a search client to integrate with Fumadocs UI.

## MDX Remote

Fumadocs offers the **MDX Remote** package, it is a helper to integrate Markdown-based content sources with Fumadocs.
You can think it as a `next-mdx-remote` with built-in plugins for Fumadocs.

### Setup

```package-install
@fumadocs/mdx-remote
```

The main feature it offers is the MDX Compiler, it can compile MDX content to JSX nodes.
Since it doesn't use a bundler, there's some limitations:

- No imports and exports in MDX files.

It's compatible with Server Components. For example:

```tsx
import { compileMDX } from '@fumadocs/mdx-remote';
import { getPage } from './my-content-source';
import { DocsBody, DocsPage } from 'fumadocs-ui/page';
import { getMDXComponents } from '@/mdx-components';

export default async function Page({
  params,
}: {
  params: { slug?: string[] };
}) {
  const page = getPage(params.slug);
  const compiled = await compileMDX({
    source: page.content,
  });

  const MdxContent = compiled.body;

  return (
    <DocsPage toc={compiled.toc}>
      <DocsBody>
        <MdxContent components={getMDXComponents()} />
      </DocsBody>
    </DocsPage>
  );
}
```

#### Images

On some platforms like Vercel, the original `public` folder (including static assets like images) will be removed after `next build`.
`compileMDX` might no longer be able to access local images in `public`.

When referencing images, make sure to use a URL.
`````

## File: apps/docs/content/docs/headless/index.mdx
`````
---
title: Introduction
description: Getting started with core library
icon: Album
---

## What is this?

Fumadocs Core offers server-side functions and headless components to build docs on any React.js frameworks like Next.js.

- Search (built-in: Orama, Algolia Search)
- Breadcrumb, Sidebar, TOC Components
- Remark/Rehype Plugins
- Additional utilities

<Callout title="Tip">

    It can be used without Fumadocs UI, in other words, it's headless.

    For beginners and normal usages, use [Fumadocs UI](/docs/ui).

</Callout>

## Installation

No other dependencies required.

```package-install
fumadocs-core
```

For some components, a framework provider is needed:

```tsx tab="Next.js"
import type { ReactNode } from 'react';
import { NextProvider } from 'fumadocs-core/framework/next';

export function RootLayout({ children }: { children: ReactNode }) {
  // or if you're using Fumadocs UI, use `<RootProvider />`
  return <NextProvider>{children}</NextProvider>;
}
```

```tsx tab="React Router"
import type { ReactNode } from 'react';
import { ReactRouterProvider } from 'fumadocs-core/framework/react-router';

export function Root({ children }: { children: ReactNode }) {
  return <ReactRouterProvider>{children}</ReactRouterProvider>;
}
```

```tsx tab="Tanstack Start/Router"
import type { ReactNode } from 'react';
import { TanstackProvider } from 'fumadocs-core/framework/tanstack';

export function Root({ children }: { children: ReactNode }) {
  return <TanstackProvider>{children}</TanstackProvider>;
}
```

It offers simple document searching as well as components for building a
good docs.

<Cards>

<Card
  title="Breadcrumb"
  href="/docs/headless/components/breadcrumb"
  description="The navigation component at the top of screen"
/>

<Card
  title="TOC"
  href="/docs/headless/components/toc"
  description="A Table of Contents with active anchor observer"
/>

<Card
  title="Sidebar"
  href="/docs/headless/components/sidebar"
  description="The navigation bar at aside of viewport"
/>

<Card
  title="Search"
  href="/docs/headless/search"
  description="Implement document searching"
/>

</Cards>
`````

## File: apps/docs/content/docs/headless/internationalization.mdx
`````
---
title: Internationalization
description: Support multiple languages in your documentation
---

## Introduction

Fumadocs core provides necessary middleware and options for i18n support.

You can define a config to share between utilities.

<include cwd meta='title="lib/i18n.ts"'>
  ../../examples/i18n/lib/i18n.ts
</include>

### Hide Locale Prefix

To hide the locale prefix (e.g. `/en/page` -> `/page`), use the `hideLocale` option.

```ts
import type { I18nConfig } from 'fumadocs-core/i18n';

export const i18n: I18nConfig = {
  defaultLanguage: 'en',
  languages: ['en', 'cn'],
  hideLocale: 'default-locale',
};
```

| Mode             | Description                                        |
| ---------------- | -------------------------------------------------- |
| `always`         | Always hide the prefix, detect locale from cookies |
| `default-locale` | Only hide the default locale                       |
| `never`          | Never hide the prefix (default)                    |

<Callout type='warn' title={<>Using <code>always</code></>}>

On `always` mode, locale is stored as a cookie (set by the middleware), which isn't optimal for static sites.

This may cause undesired cache problems, and need to pay extra attention on SEO to ensure search engines can index your pages correctly.

</Callout>

### Middleware

Redirects users to appropriate locale, it can be customised from `i18n.ts`.

<include cwd meta='title="middleware.ts"'>
  ../../examples/i18n/middleware.ts
</include>

> When `hideLocale` is enabled, it uses `NextResponse.rewrite` to hide locale prefixes.
`````

## File: apps/docs/content/docs/headless/page-conventions.mdx
`````
---
title: Routing
description: A shared convention for organizing your documents
---

<Callout title='Before reading'>

    This guide only applies for content sources that uses `loader()` API, such as Fumadocs MDX.

</Callout>

## Overview

While Next.js handles routing, Fumadocs generates **page slugs** and **sidebar items** (page tree) from your content directory using [`loader()`](/docs/headless/source-api).

You can define folders and pages similar to the file-system based routing of Next.js.

<Files>
  <Folder name="content/docs (content directory)" defaultOpen>
    <File name="index.mdx" />
    <File name="getting-started.mdx" />
  </Folder>
</Files>

## File

A [MDX](https://mdxjs.com) or Markdown file, you can customise its frontmatter.

```mdx
---
title: My Page
description: Best document ever
icon: HomeIcon
full: true
---

## Learn More
```

| name          | description                                        |
| ------------- | -------------------------------------------------- |
| `title`       | The title of page                                  |
| `description` | The description of page                            |
| `icon`        | The name of icon, see [Icons](#icons)              |
| `full`        | Fill all available space on the page (Fumadocs UI) |

<Callout title='Fumadocs MDX'>

    You can use the [`schema`](/docs/mdx/collections#schema-1) option to add frontmatter properties.

</Callout>

### Slugs

The slugs of a page are generated from its file path.

| path (relative to content folder) | slugs             |
| --------------------------------- | ----------------- |
| `./dir/page.mdx`                  | `['dir', 'page']` |
| `./dir/index.mdx`                 | `['dir']`         |

## Folder

Organize multiple pages, you can create a [Meta file](#meta) to customise folders.

### Folder Group

By default, putting a file into folder will change its slugs.
You can wrap the folder name in parentheses to avoid impacting the slugs of child files.

| path (relative to content folder) | slugs      |
| --------------------------------- | ---------- |
| `./(group-name)/page.mdx`         | `['page']` |

## Meta

Customise folders by creating a `meta.json` file in the folder.

```json title="meta.json"
{
  "title": "Display Name",
  "icon": "MyIcon",
  "pages": ["index", "getting-started"],
  "defaultOpen": true
}
```

| name          | description                           |
| ------------- | ------------------------------------- |
| `title`       | Display name                          |
| `icon`        | The name of icon, see [Icons](#icons) |
| `pages`       | Folder items (see below)              |
| `defaultOpen` | Open the folder by default            |

### Pages

By default, folder items are sorted alphabetically.

You can add or control the order of items using `pages`, items are not included unless they are listed inside.

```json title="meta.json"
{
  "title": "Name of Folder",
  "pages": ["guide", "components", "---My Separator---", "./nested/page"]
}
```

<Files>
  <File name="meta.json" />
  <File name="guide.mdx" />
  <File name="components.mdx" />
  <File name="nested/page.mdx" />
</Files>

#### Rest

Add a `...` item to include remaining pages (sorted alphabetically), or `z...a` for descending order.

```json title="meta.json"
{
  "pages": ["guide", "..."]
}
```

You can add `!name` to prevent an item from being included.

```json title="meta.json"
{
  "pages": ["guide", "...", "!components"]
}
```

#### Extract

You can extract the items from a folder with `...folder_name`.

```json title="meta.json"
{
  "pages": ["guide", "...nested"]
}
```

#### Link

Use the syntax `[Text](url)` to insert links, or `[Icon][Text](url)` to add icon.

```json title="meta.json"
{
  "pages": [
    "[Vercel](https://vercel.com)",
    "[Triangle][Vercel](https://vercel.com)"
  ]
}
```

## Icons

Since Fumadocs doesn't include an icon library, you have to convert the icon names to JSX elements in runtime, and render it as a component.

You can add an [`icon` handler](/docs/headless/source-api#icons) to `loader()`.

## Root Folder

Marks the folder as a root folder, only items in the opened root folder will be considered.

```json title="meta.json"
{
  "title": "Name of Folder",
  "description": "The description of root folder (optional)",
  "root": true
}
```

For example, when you are opening a root folder `framework`, the other folders (e.g. `headless`) are not shown on the sidebar and other navigation elements.

<Files>
  <Folder name="framework" defaultOpen>
    <File name="index.mdx" />
    <File
      name="current-page.mdx"
      className="!text-fd-primary !bg-fd-primary/10"
    />
    <File name="other-pages.mdx" />
  </Folder>
  <Folder name="headless (hidden)" className="opacity-50" disabled defaultOpen>
    <File name="my-page.mdx" />
  </Folder>
</Files>

<Callout title='Fumadocs UI'>

    Fumadocs UI renders root folders as [Sidebar Tabs](/docs/ui/navigation/sidebar#sidebar-tabs), which allows user to switch between them.

</Callout>

## Internationalization

<include>../../shared/page-conventions.i18n.mdx</include>
`````

## File: apps/docs/content/docs/headless/page-tree.mdx
`````
---
title: Page Tree
description: The structure of page tree.
---

Page tree is a tree structure that describes all navigation links, with other items like separator and folders.

It will be sent to the client and being referenced in navigation elements including the sidebar and breadcrumb.
Hence, you shouldn't store any sensitive or large data in page tree.

<Callout title="Note">

By design, page tree only contains necessary information of all pages and folders.

Unserializable data such as functions can't be passed to page tree.

</Callout>

## Conventions

The type definitions of page tree, for people who want to hardcode/generate it.
You can also import the type from Fumadocs.

```ts
import type { PageTree } from 'fumadocs-core/server';

const tree: PageTree.Root = {
  // props
};
```

Certain nodes contain a `$ref` property, they are internal and not used when hardcoding it.

### Root

The initial root of page trees.

<AutoTypeTable path="./content/docs/headless/props.ts" name="PageTreeRoot" />

### Page

```json
{
  "type": "page",
  "name": "Quick Start",
  "url": "/docs"
}
```

> External urls are also supported

<AutoTypeTable path="./content/docs/headless/props.ts" name="PageTreeItem" />

### Folder

```json
{
    "type": "folder",
    "name": "Guide",
    "index": {
        "type": "page",
        ...
    }
    "children": [
        ...
    ]
}
```

<AutoTypeTable path="./content/docs/headless/props.ts" name="PageTreeFolder" />

### Separator

A label between items.

```json
{
  "type": "separator",
  "name": "Components"
}
```

<AutoTypeTable
  path="./content/docs/headless/props.ts"
  name="PageTreeSeparator"
/>

## Icons

Icon is a `ReactElement`, supported by pages and folders.
`````

## File: apps/docs/content/docs/headless/source-api.mdx
`````
---
title: loader()
description: Turn a content source into a unified interface
---

## Usage

`loader()` provides an interface for Fumadocs to integrate with file-system based content sources.

### What it does?

- Generate page trees based on file system.
- Assign URL and slugs to each page.
- Output useful utilities to interact with content.

It doesn't rely on the real file system (zero `node:fs` usage), a virtual storage is also allowed.

You can use it with built-in content sources like Fumadocs MDX.

```ts
import { loader } from 'fumadocs-core/source';
import { docs } from '@/.source';

export const source = loader({
  source: docs.toFumadocsSource(),
});
```

### URL

You can override the base URL, or specify a function to generate URL for each page.

```ts
import { loader } from 'fumadocs-core/source';

loader({
  baseUrl: '/docs',
  // or you can customise it with function
  url(slugs, locale) {
    if (locale) return '/' + [locale, 'docs', ...slugs].join('/');
    return '/' + ['docs', ...slugs].join('/');
  },
});
```

### Icons

Load the [icon](/docs/headless/page-conventions#icons) property specified by pages and meta files.

```ts
import { loader } from 'fumadocs-core/source';
import { icons } from 'lucide-react';
import { createElement } from 'react';

loader({
  icon(icon) {
    if (!icon) {
      // You may set a default icon
      return;
    }

    if (icon in icons) return createElement(icons[icon as keyof typeof icons]);
  },
});
```

### I18n

Pass the `i18n` config to loader.

```ts title="lib/source.ts"
import { i18n } from '@/lib/i18n';
import { loader } from 'fumadocs-core/source';

export const source = loader({
  i18n, // [!code highlight]
});
```

With i18n enabled, loader will generate a page tree for every locale.

When looking for a page, it fallbacks to default locale if the page doesn't exist for specified locale.

## Output

The loader outputs a source object.

### Get Page

Get page with slugs.

```ts
import { source } from '@/lib/source';

source.getPage(['slug', 'of', 'page']);

// with i18n
source.getPage(['slug', 'of', 'page'], 'locale');
```

### Get Pages

Get a list of page available for locale.

```ts
import { source } from '@/lib/source';

// from default locale
source.getPages();

// for a specific locale
source.getPages('locale');
```

### Page Tree

```ts
import { source } from '@/lib/source';

// without i18n
source.pageTree;

// with i18n
source.pageTree['locale'];
```

### Get from Node

The page tree nodes contain references to their original file path.
You can find their original page or meta file from the tree nodes.

```ts
import { source } from '@/lib/source';

source.getNodePage(pageNode);
source.getNodeMeta(folderNode);
```

### Params

A function to generate output for Next.js `generateStaticParams`.
The generated parameter names will be `slug: string[]` and `lang: string` (i18n only).

```ts title="app/[[...slug]]/page.tsx"
import { source } from '@/lib/source';

export function generateStaticParams() {
  return source.generateParams();
}
```

### Language Entries

Get available languages and its pages.

```ts
import { source } from '@/lib/source';

// language -> pages
const entries = source.getLanguages();
```

## Deep Dive

As mentioned, Source API doesn't rely on real file systems.
During the process, your input source files will be parsed and form a virtual storage to avoid inconsistent behaviour between different OS.

### Transformer

To perform virtual file-system operations before processing, you can add a transformer.

```ts
import { loader } from 'fumadocs-core/source';

loader({
  transformers: [
    ({ storage }) => {
      storage.makeDir();
    },
  ],
});
```

### Page Tree

The page tree is generated from your file system, some unnecessary information (e.g. unused frontmatter properties) will be filtered.

You can customise it using the `pageTree` option, such as attaching custom properties to nodes, or customising the display name of pages.

```tsx
import React from 'react';
import { loader } from 'fumadocs-core/source';

loader({
  pageTree: {
    attachFile(node, file) {
      // you can access its file information
      console.log(file?.data);
      // JSX nodes are allowed
      node.name = <>Some JSX Nodes here</>;

      return node;
    },
  },
});
```

### Custom Source

To plug your own content source, create a `Source` object.

It includes a `files` property which is an array of virtual files.
Each virtual file must contain its file path and corresponding data.
You can check type definitions for more info.

Since Source API doesn't rely on file system, file paths cannot be absolute or relative (for example, `./file.mdx` and `D://content/file.mdx` are not allowed).
Instead, pass the file paths like `file.mdx` and `content/file.mdx`.

```ts
import { Source } from 'fumadocs-core/source';

export function createMySource(): Source<{
  metaData: { title: string; pages: string[] }; // Your custom type
  pageData: { title: string; description: string }; // Your custom type
}> {
  return {
    files: [],
  };
}
```
`````

## File: apps/docs/content/docs/mdx/(integrations)/vite/react-router.mdx
`````
---
title: React Router
description: Use Fumadocs MDX with React Router
---

## Setup

```npm
npm i fumadocs-mdx fumadocs-core @types/mdx
```

Create the configuration file:

<include cwd meta='title="source.config.ts"'>
  ../../examples/react-router/source.config.ts
</include>

Add the Vite plugin:

<include cwd meta='title="vite.config.ts"'>
  ../../examples/react-router/vite.config.ts
</include>

A `source.generated.ts` file will be generated when you run development server or production build.

### Accessing Content

You can import the `source.generated.ts` file directly.

```ts
import { docs } from './source.generated';
console.log(docs);
```

To integrate with Fumadocs, create a docs collection and use:

<include cwd meta='title="app/source.ts"'>
  ../../examples/react-router/app/source.ts
</include>

### Rendering Content

Rendering page content is different because React Router doesn't support RSC at the moment.
Instead, use `toClientRenderer()` to lazy load MDX content as a component on browser.

For example:

<include cwd meta='title="app/docs/page.tsx"'>
  ../../examples/react-router/app/docs/page.tsx
</include>
`````

## File: apps/docs/content/docs/mdx/(integrations)/vite/tanstack.mdx
`````
---
title: Tanstack Start
description: Use Fumadocs MDX with Tanstack Start & Router
---

## Setup

```npm
npm i fumadocs-mdx fumadocs-core @types/mdx
```

Create the configuration file:

<include cwd meta='title="source.config.ts"'>
  ../../examples/tanstack-start/source.config.ts
</include>

Add the Vite plugin:

<include cwd meta='title="vite.config.ts"'>
  ../../examples/tanstack-start/vite.config.ts
</include>

A `source.generated.ts` file will be generated when you run development server or production build.

### Accessing Content

You can import the `source.generated.ts` file directly.

```ts
import { docs } from './source.generated';
console.log(docs);
```

To integrate with Fumadocs, create a docs collection and use:

```ts title="src/lib/source.ts"
import { loader } from 'fumadocs-core/source';
import { create, docs } from '../../source.generated';

export const source = loader({
  source: await create.sourceAsync(docs.doc, docs.meta),
  baseUrl: '/docs',
});
```

### Rendering Content

As Tanstack Start doesn't support RSC at the moment, use `createClientLoader()` to lazy load MDX content as a component on browser.

For example:

```tsx title="src/routes/docs/$.tsx"
import { createFileRoute, notFound } from '@tanstack/react-router';
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import { createServerFn } from '@tanstack/react-start';
import { source } from '~/lib/source';
import { docs } from '../../../source.generated';
import {
  DocsBody,
  DocsDescription,
  DocsPage,
  DocsTitle,
} from 'fumadocs-ui/page';
import defaultMdxComponents from 'fumadocs-ui/mdx';
import { createClientLoader } from 'fumadocs-mdx/runtime/vite';

export const Route = createFileRoute('/docs/$')({
  component: Page,
  loader: async ({ params }) => {
    const data = await loader({ data: params._splat?.split('/') ?? [] });
    await clientLoader.preload(data.path);
    return data;
  },
});

const loader = createServerFn({
  method: 'GET',
})
  .validator((slugs: string[]) => slugs)
  .handler(async ({ data: slugs }) => {
    const page = source.getPage(slugs);
    if (!page) throw notFound();

    return {
      tree: source.pageTree as object,
      path: page.path,
    };
  });

const clientLoader = createClientLoader(docs.doc, {
  id: 'docs',
  component({ toc, frontmatter, default: MDX }) {
    return (
      <DocsPage toc={toc}>
        <DocsTitle>{frontmatter.title}</DocsTitle>
        <DocsDescription>{frontmatter.description}</DocsDescription>
        <DocsBody>
          <MDX
            components={{
              ...defaultMdxComponents,
            }}
          />
        </DocsBody>
      </DocsPage>
    );
  },
});

function Page() {
  const data = Route.useLoaderData();
  const Content = clientLoader.getComponent(data.path);

  return (
    <DocsLayout
      tree={data.tree}
      nav={{
        title: 'Fumadocs Tanstack',
      }}
    >
      <Content />
    </DocsLayout>
  );
}
```
`````

## File: apps/docs/content/docs/mdx/(integrations)/next.mdx
`````
---
title: Next.js
description: Use Fumadocs MDX with Next.js
---

## Setup

Set up Fumadocs MDX for your Next.js application.

```npm
npm i fumadocs-mdx @types/mdx @types/mdx
```

Create the configuration file:

```ts title="source.config.ts"
import { defineDocs, defineConfig } from 'fumadocs-mdx/config';

export const docs = defineDocs({
  dir: 'content/docs',
});

export default defineConfig();
```

Add the plugin to Next.js config:

```js title="next.config.mjs"
import { createMDX } from 'fumadocs-mdx/next';

const withMDX = createMDX({
  // customise the config file path
  // configPath: "source.config.ts"
});

/** @type {import('next').NextConfig} */
const config = {
  reactStrictMode: true,
};

export default withMDX(config);
```

<Callout title="ESM Only" type='warn' className="mt-4">

    The Next.js config must be a `.mjs` file since Fumadocs is ESM-only.

</Callout>

A `.source` folder will be generated when you run `next dev` or `next build`.

### Accessing Content

You can access the collection output from `.source` folder with its original name:

```ts tab="source.config.ts"
import { defineDocs } from 'fumadocs-mdx/config';

export const docs = defineDocs({
  dir: 'content/docs',
  docs: {
    // options for `doc` collection
  },
  meta: {
    // options for `meta` collection
  },
});
```

```ts tab="Usage"
import { docs } from '@/.source';

console.log(docs);
```

The type of output can have a different type/shape depending on the collection type and schema.

> Make sure you are importing from `.source` rather than `source.config.ts`. We will import it with `@/.source` import alias in this guide.

### Integrate with Fumadocs

Create a `docs` collection and use `toFumadocsSource()` on the output.

```ts title="lib/source.ts"
import { docs } from '@/.source';
import { loader } from 'fumadocs-core/source';

export const source = loader({
  baseUrl: '/docs',
  source: docs.toFumadocsSource(),
});
```

> You can do the same for multiple `docs` collections.

Generally, you'll interact with the collection through [`loader()`](/docs/headless/source-api#output).

```tsx
import { source } from '@/lib/source';

const page = source.getPage(['slugs']);

if (page) {
  // access page data [!code highlight]
  console.log(page.data);

  // frontmatter properties are also inside [!code highlight]
  console.log(page.data.title);
}
```

To render the page, use `page.data.body` as a component.

```tsx
import { getMDXComponents } from '@/mdx-components';

const MDX = page.data.body;

// set your MDX components with `components` prop
return <MDX components={getMDXComponents()} />;
```

### Integrate with CI

The `fumadocs-mdx` command also generates types for `.source` folder. Add it as a post install script to ensure types are generated when initializing the project.

```json title="package.json"
{
  "scripts": {
    "postinstall": "fumadocs-mdx"
  }
}
```
`````

## File: apps/docs/content/docs/mdx/async.mdx
`````
---
title: Async Mode
description: Runtime compilation of content files.
---

## Introduction

By default, all Markdown and MDX files need to be pre-compiled first. The same constraint also applies to the development server.

This may result in longer dev server start times for large docs sites. You can enable Async Mode on `doc` collections to improve this.

### Setup

Install required dependencies.

```package-install
@fumadocs/mdx-remote shiki
```

Enable Async Mode.

```ts tab="Docs Collection"
import { defineDocs } from 'fumadocs-mdx/config';

export const docs = defineDocs({
  dir: 'content/docs',
  docs: {
    async: true,
  },
});
```

```ts tab="Doc Collection"
import { defineCollections } from 'fumadocs-mdx/config';

export const doc = defineCollections({
  type: 'doc',
  dir: 'content/docs',
  async: true,
});
```

### Usage

Async Mode allows on-demand compilation of Markdown and MDX content by moving the compilation process from build time to Next.js runtime.

However, you need to invoke the `load()` async function to load and compile content.

For example:

```tsx title="lib/source.ts"
import { loader } from 'fumadocs-core/source';
import { docs } from '@/.source';

export const source = loader({
  baseUrl: '/docs',
  source: docs.toFumadocsSource(),
});
```

```tsx title="page.tsx"
import { source } from '@/lib/source';
import { getMDXComponents } from '@/mdx-components';

const page = source.getPage(['...']);

if (page) {
  // frontmatter properties are available
  console.log(page.data);

  // Markdown content requires await
  const { body: MdxContent, toc } = await page.data.load();

  console.log(toc);

  return <MdxContent components={getMDXComponents()} />;
}
```

When using Async Mode, we highly recommend to use third-party services to implement search, which usually have better capability to handle massive amount of content to index.

### Constraints

It comes with some limitations on MDX features.

- No import/export allowed in MDX files. For MDX components, pass them from the `components` prop instead.
- Images must be referenced with URL (e.g. `/images/test.png`). Don't use **file paths** like `./image.png`. You should locate your images in the `public` folder and reference them with URLs.
`````

## File: apps/docs/content/docs/mdx/collections.mdx
`````
---
title: Collections
description: Collection of content data for your app
---

## Define Collections

Define a collection to parse a certain set of files.

```ts
import { defineCollections } from 'fumadocs-mdx/config';
import { z } from 'zod';

export const blog = defineCollections({
  type: 'doc',
  dir: './content/blog',
  schema: z.object({
    // schema
  }),
  // other options
});
```

### `type`

The accepted type of collection.

```ts
import { defineCollections } from 'fumadocs-mdx/config';

// only scan for json/yaml files
export const metaFiles = defineCollections({
  type: 'meta',
  // options
});
```

- `type: meta`

  Accept JSON/YAML files, available options:

  <AutoTypeTable path="./content/docs/mdx/props.ts" name="MetaCollection" />

- `type: doc`

  Markdown/MDX documents, available options:

  <AutoTypeTable path="./content/docs/mdx/props.ts" name="DocCollection" />

### `dir`

Directories to scan for input files.

### `schema`

The schema to validate file data (frontmatter on `doc` type, content on `meta` type).

```ts
import { defineCollections } from 'fumadocs-mdx/config';
import { z } from 'zod';

export const blog = defineCollections({
  type: 'doc',
  dir: './content/blog',
  schema: z.object({
    name: z.string(),
  }),
});
```

> [Standard Schema](https://standardschema.dev) compatible libraries, including Zod, are supported.

Note that the validation is done at build time, hence the output must be serializable.
You can also pass a function that receives the transform context.

```ts
import { defineCollections } from 'fumadocs-mdx/config';
import { z } from 'zod';

export const blog = defineCollections({
  type: 'doc',
  dir: './content/blog',
  schema: (ctx) => {
    return z.object({
      name: z.string(),
      testPath: z.string().default(
        // original file path
        ctx.path,
      ),
    });
  },
});
```

### `mdxOptions`

Customise MDX options at the collection level.

```ts title="source.config.ts"
import { defineCollections, getDefaultMDXOptions } from 'fumadocs-mdx/config';

export const blog = defineCollections({
  type: 'doc',
  mdxOptions: {
    // mdx options
  },
});
```

By design, this will remove all default settings applied by your global config and Fumadocs MDX.
You have full control over MDX options.

You can use `getDefaultMDXOptions` to apply default configurations, it accepts the [extended MDX Options](/docs/mdx/mdx#extended).

```ts title="source.config.ts"
import { defineCollections, getDefaultMDXOptions } from 'fumadocs-mdx/config';

export const blog = defineCollections({
  type: 'doc',
  mdxOptions: getDefaultMDXOptions({
    // extended mdx options
  }),
});
```

> This API is only available on `doc` type.

## Define Docs

Define a collection for Fumadocs.

```ts
import { defineDocs } from 'fumadocs-mdx/config';

export const docs = defineDocs({
  dir: '/my/content/dir',
  docs: {
    // optional, options of `doc` collection
  },
  meta: {
    // optional, options of `meta` collection
  },
});
```

### `dir`

Instead of per collection, you should customise `dir` from `defineDocs`:

```ts
import { defineDocs } from 'fumadocs-mdx/config';

export const docs = defineDocs({
  dir: 'my/content/dir',
});
```

### `schema`

You can extend the default Zod schema of `docs` and `meta`.

```ts
import { frontmatterSchema, metaSchema, defineDocs } from 'fumadocs-mdx/config';
import { z } from 'zod';

export const docs = defineDocs({
  docs: {
    schema: frontmatterSchema.extend({
      index: z.boolean().default(false),
    }),
  },
  meta: {
    schema: metaSchema.extend({
      // other props
    }),
  },
});
```
`````

## File: apps/docs/content/docs/mdx/global.mdx
`````
---
title: Global Options
description: Customise Fumadocs MDX
---

## Global Options

Shared options of Fumadocs MDX.

```ts title="source.config.ts"
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  // global options
});
```

<AutoTypeTable path="./content/docs/mdx/props.ts" name="GlobalConfig" />

### MDX Options

Customise the default MDX processor options, it accepts the [extended MDX options](/docs/mdx/mdx#extended).

```ts title="source.config.ts"
import { defineConfig } from 'fumadocs-mdx/config';
import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math';

export default defineConfig({
  mdxOptions: {
    remarkPlugins: [remarkMath],
    // When order matters
    rehypePlugins: (v) => [rehypeKatex, ...v],
  },
});
```

Some default options are applied by Fumadocs MDX, you can also disable them:

```ts title="source.config.ts"
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    preset: 'minimal',
    // now it accepts only MDX processor options
  },
});
```
`````

## File: apps/docs/content/docs/mdx/include.mdx
`````
---
title: Include
description: Reuse content from other files.
---

## Usage

### Markdown

Specify the target Markdown file path in the `<include>` tag (relative to the Markdown file itself).

```mdx title="page.mdx"
<include>./another.mdx</include>
```

This will display the content from the target file (e.g. `another.mdx`).

### CodeBlock

For other types of files, it will become a codeblock:

```mdx title="page.mdx"
<include>./script.ts</include>

<include lang="tsx" meta='title="lib.ts"'>
  ./script.ts
</include>
```

### `cwd`

Resolve relative paths from cwd instead of the Markdown file:

```mdx
<include cwd lang="tsx" meta='title="lib.ts"'>
  ./script.ts
</include>
```
`````

## File: apps/docs/content/docs/mdx/index.mdx
`````
---
title: Getting Started
description: Introducing Fumadocs MDX, the official content source of Fumadocs.
icon: Album
---

## Quick Start

Get started with Fumadocs MDX:

<Cards>
  <Card title="Next.js" href="/docs/mdx/next">
    Using Fumadocs MDX with Next.js.
  </Card>
  <Card title="React Router" href="/docs/mdx/vite/react-router">
    Using Fumadocs MDX with React Router 7 or above.
  </Card>
  <Card title="Tanstack Start" href="/docs/mdx/vite/tanstack">
    Using Fumadocs MDX with Tanstack Start/Router.
  </Card>
</Cards>

## Introduction

Fumadocs MDX is a tool to transform content into type-safe data, similar to Content Collections.

It is not a full CMS but rather a content compiler + validator, you can use it to handle blog posts and other contents.

### Defining Collections

**Collection** refers to a collection containing a certain type of files. You can define collections in the config file (`source.config.ts`).

Fumadocs MDX transforms collections into type-safe data, accessible in your app. Available collections:

<Tabs items={["doc", "meta", 'docs']}>

    <Tab value='doc'>

Compile Markdown & MDX files into a React Server Component, with useful properties like **Table of Contents**.

```ts title="source.config.ts"
import { defineCollections } from 'fumadocs-mdx/config';

export const test = defineCollections({
  type: 'doc',
  dir: 'content/docs',
});
```

    </Tab>

    <Tab value='meta'>

Transform YAML/JSON files into an array of data.

```ts title="source.config.ts"
import { defineCollections } from 'fumadocs-mdx/config';

export const test = defineCollections({
  type: 'meta',
  dir: 'content/docs',
});
```

    </Tab>
    <Tab value='docs'>

Combination of `meta` and `doc` collections, which is needed for Fumadocs.

```ts title="source.config.ts"
import { defineDocs } from 'fumadocs-mdx/config';

export const docs = defineDocs({
  dir: 'content/docs',
  docs: {
    // options for `doc` collection
  },
  meta: {
    // options for `meta` collection
  },
});
```

    </Tab>

</Tabs>

For example, a `doc` collection will transform the `.md` and `.mdx` files:

<Files>
  <Folder name="folder" defaultOpen>
    <File name="ui.md" />
  </Folder>
  <File name="hello.md" />
  <File name="index.mdx" />
  <File
    name="meta.json"
    className="opacity-50 cursor-not-allowed"
    aria-disabled
  />
</Files>

### Accessing Collections

Collections will be compiled into JavaScript files that your app can access, the output format varies according to the framework you use.

[Get started](#quickstart) with your framework to learn more.

## FAQ

### Built-in Properties

These properties are exported from MDX files by default.

| Property         | Description                                     |
| ---------------- | ----------------------------------------------- |
| `frontmatter`    | Frontmatter                                     |
| `toc`            | Table of Contents                               |
| `structuredData` | Structured Data, useful for implementing search |

### Customise Frontmatter

Use the [`schema`](/docs/mdx/collections#schema-1) option to pass a validation schema to validate frontmatter and define its output properties.

### MDX Plugins

Fumadocs MDX uses [MDX Compiler](https://mdxjs.com/packages/mdx) to compile MDX files into JavaScript files.

You can customise it on [Global Config](/docs/mdx/global#mdx-options) or [Collection Config](/docs/mdx/collections#mdxoptions).
`````

## File: apps/docs/content/docs/mdx/last-modified.mdx
`````
---
title: Last Modified Time
description: Output the last modified time of a document
---

## Usage

This feature is not enabled by default, you can enable this from the config file. Note that it only supports Git as version control.
Please ensure you have Git installed on your machine, and **the repository is not shallow cloned**, as it relies on your local Git history.

```ts title="source.config.ts"
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  lastModifiedTime: 'git', // [!code highlight]
});
```

### Access the Property

After doing this, a `lastModified` number will be exported for each document. You can convert it to a JavaScript Date object.

```ts
import { source } from '@/lib/source';

const page = source.getPage(['...']);

console.log(new Date(page.data.lastModified));
// or with async mode:
const { lastModified } = await page.data.load();
console.log(new Date(lastModified));
```
`````

## File: apps/docs/content/docs/mdx/mdx.mdx
`````
---
title: Default MDX Config
description: Customise the default configurations for MDX processor.
---

## Extended MDX Options [#extended]

Fumadocs MDX will apply some default MDX options, to make features like **syntax highlighting** work out of the box.

To allow overriding the defaults, Fumadocs MDX supports **Extended MDX Options** on top of [`ProcessorOptions`](https://mdxjs.com/packages/mdx/#processoroptions).
Additional options below:

### Remark Plugins

These plugins are applied by default:

- [Remark Image](/docs/headless/mdx/remark-image) - Handle images
- [Remark Heading](/docs/headless/mdx/headings) - Extract table of contents
- [Remark Structure](/docs/headless/mdx/structure) - Generate search indexes
- Remark Exports - Exports the output generated by remark plugins above

Add other remark plugins with:

```ts tab="Global Config"
import { defineConfig } from 'fumadocs-mdx/config';
import { myPlugin } from './remark-plugin';

export default defineConfig({
  mdxOptions: {
    remarkPlugins: [myPlugin],
    // You can also pass a function to control the order of remark plugins.
    remarkPlugins: (v) => [myPlugin, ...v],
  },
});
```

```ts tab="Collection Config"
import { defineCollections, getDefaultMDXOptions } from 'fumadocs-mdx/config';
import { myPlugin } from './remark-plugin';

export const blog = defineCollections({
  type: 'doc',
  mdxOptions: getDefaultMDXOptions({
    remarkPlugins: [myPlugin],
    // You can also pass a function to control the order of remark plugins.
    remarkPlugins: (v) => [myPlugin, ...v],
  }),
});
```

### Rehype Plugins

These plugins are applied by default:

- [Rehype Code](/docs/headless/mdx/rehype-code) - Syntax highlighting

Same as remark plugins, you can pass an array or a function to add other rehype plugins.

```ts tab="Global Config"
import { defineConfig } from 'fumadocs-mdx/config';
import { myPlugin } from './rehype-plugin';

export default defineConfig({
  mdxOptions: {
    rehypePlugins: (v) => [myPlugin, ...v],
  },
});
```

```ts tab="Collection Config"
import { defineCollections, getDefaultMDXOptions } from 'fumadocs-mdx/config';
import { myPlugin } from './rehype-plugin';

export const blog = defineCollections({
  type: 'doc',
  mdxOptions: getDefaultMDXOptions({
    rehypePlugins: (v) => [myPlugin, ...v],
  }),
});
```

### Customise Built-in Plugins

Customise the options of built-in plugins like:

```ts tab="Global Config"
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    rehypeCodeOptions: {
      // options
    },
    remarkImageOptions: {
      // options
    },
    remarkHeadingOptions: {
      // options
    },
  },
});
```

```ts tab="Collection Config"
import { defineCollections, getDefaultMDXOptions } from 'fumadocs-mdx/config';

export const blog = defineCollections({
  type: 'doc',
  mdxOptions: getDefaultMDXOptions({
    rehypeCodeOptions: {
      // options
    },
    remarkImageOptions: {
      // options
    },
    remarkHeadingOptions: {
      // options
    },
  }),
});
```

### Export Properties from `vfile.data`

Some remark plugins store their output in `vfile.data` (compile-time memory) which cannot be accessed from your code.
Fumadocs MDX applies a remark plugin that turns `vfile.data` properties into ESM exports, so you can access these properties when importing the MDX file.

You can define additional properties to be exported.

```ts tab="Global Config"
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    valueToExport: ['dataName'],
  },
});
```

```ts tab="Collection Config"
import { defineCollections, getDefaultMDXOptions } from 'fumadocs-mdx/config';

export const blog = defineCollections({
  type: 'doc',
  mdxOptions: getDefaultMDXOptions({
    valueToExport: ['dataName'],
  }),
});
```

By default, it includes:

- `toc` for the Remark Heading plugin
- `structuredData` for the Remark Structure Plugin
- `frontmatter` for the frontmatter of MDX (using `gray-matter`)
`````

## File: apps/docs/content/docs/mdx/page.mdx
`````
---
title: Use as Page
description: Use MDX file as a page
---

## Setup

You can use `page.mdx` instead of `page.tsx` for creating a new page under the app directory.

However, it doesn't have MDX components by default, so you have to provide them:

```tsx title="mdx-components.tsx"
import defaultMdxComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultMdxComponents, // for Fumadocs UI
    ...components,
  };
}

// export a `useMDXComponents()` that returns MDX components
export const useMDXComponents = getMDXComponents; // [!code ++]
```

```ts title="source.config.ts"
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    // Path to import your `mdx-components.tsx` above. [!code ++]
    providerImportSource: '@/mdx-components',
  },
});
```

### Usage

```mdx title="app/test/page.mdx"
{/* this will enable Typography styles of Fumadocs UI */}
export { withArticle as default } from 'fumadocs-ui/page';

## Hello World
```
`````

## File: apps/docs/content/docs/mdx/performance.mdx
`````
---
title: Performance
description: The performance of Fumadocs MDX
icon: Rocket
---

## Overview

Fumadocs MDX is a bundler plugin, in other words, it has a higher performance bottleneck.
With bundlers like Webpack and Turbopack, it is enough for large docs sites with nearly 500+ MDX files, which is sufficient for almost all use cases.

Since Fumadocs MDX works with your bundler, you can import any files including client components in your MDX files.
This allows high flexibility and ensures everything is optimized by default.

### Image Optimization

Fumadocs MDX resolves images into static imports with [Remark Image](/docs/headless/mdx/remark-image).
Therefore, your images will be optimized automatically by the Next.js Image API.

```mdx
![Hello](./hello.png)

or in public folder

![Hello](/hello.png)
```

Yields:

```mdx
import HelloImage from './hello.png';

<img alt="Hello" src={HelloImage} />
```

![Banner](/banner.png)

## Caveats

Although Fumadocs MDX can handle nearly 500+ files, it could be slow and inefficient.
A huge amount of MDX files can cause extremely high memory usage during build and development mode.

This is because of:

- Bundlers do a lot of work under the hood to bundle MDX and JavaScript files and optimize performance.
- Bundlers are not supposed to compile hundreds of MDX files.

### Solutions

The main solution is to make the compilation on-demand, such that content is only loaded when it's being requested.

#### Remote Source

Remote sources don't need to pre-compile MDX files, it can compile them on-demand with SSG which can **highly increase your build speed.**
However, you cannot use import in MDX files anymore.

See [Custom Source](/docs/headless/custom-source) for configuring remote sources.

#### Async Mode

See [Async Mode](/docs/mdx/async).
`````

## File: apps/docs/content/docs/openapi/index.mdx
`````
---
title: Scalar Example
description: View the Scalar Galaxy example OpenAPI schema.
index: true
---
`````

## File: apps/docs/content/docs/ui/(integrations)/openapi/configurations.mdx
`````
---
title: Configurations
description: Customise Fumadocs OpenAPI
---

## File Generator

Pass options to the `generateFiles` function.

### Input

An array of input files.
Allowed:

- File Paths
- External URLs
- Wildcard

```ts
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  input: ['./unkey.json'],
});
```

### Output

The output directory.

```ts
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  output: '/content/docs',
});
```

### Per

Customise how the page is generated, default to `operation`.

> Operation in OpenAPI schema refers to an API endpoint with specific method like `/api/weather:GET`.

| mode      |                             | output                                |
| --------- | --------------------------- | ------------------------------------- |
| tag       | operations with same tag    | `{tag_name}.mdx`                      |
| file      | operations in schema schema | `{file_name}.mdx`                     |
| operation | each operation              | `{operationId ?? endpoint_path}.mdx`) |

```ts
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  per: 'tag',
});
```

### Group By

In `operation` mode, you can group output files with folders.

| value | output                                                 |
| ----- | ------------------------------------------------------ |
| tag   | `{tag}/{operationId ?? endpoint_path}.mdx`             |
| route | `{endpoint_path}/{method}.mdx` (ignores `name` option) |
| none  | `{operationId ?? endpoint_path}.mdx` (default)         |

```ts
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  per: 'operation',
  groupBy: 'tag',
});
```

### Name

A function that controls the output path of MDX pages.

```ts
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  name: (output, document) => {
    if (output.type === 'operation') {
      const operation = document.paths![output.item.path]![output.item.method]!;
      // operation object
      console.log(operation);

      return 'my-dir/filename';
    }

    const hook = document.webhooks![output.item.name][output.item.method]!;
    // webhook object
    console.log(hook);
    return 'my-dir/filename';
  },
});
```

### Frontmatter

Customise the frontmatter of MDX files.

By default, it includes:

| property      | description                                      |
| ------------- | ------------------------------------------------ |
| `title`       | Page title                                       |
| `description` | Page description                                 |
| `full`        | Always true, added for Fumadocs UI               |
| `method`      | Available method of operation (`operation` mode) |
| `route`       | Route of operation (`operation` mode)            |

```ts
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  input: ['./petstore.yaml'],
  output: './content/docs',
  frontmatter: (title, description) => ({
    myProperty: 'hello',
  }),
});
```

### Add Generated Comment

Add a comment to the top of generated files indicating they are auto-generated.

```ts
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  input: ['./petstore.yaml'],
  output: './content/docs',
  // Add default comment
  addGeneratedComment: true,

  // Or provide a custom comment
  addGeneratedComment: 'Custom auto-generated comment',

  // Or disable comments
  addGeneratedComment: false,
});
```

### Tag Display Name

Adding `x-displayName` to OpenAPI Schema can control the display name of your tags.

```yaml title="openapi.yaml"
tags:
  - name: test
    description: this is a tag.
    x-displayName: My Test Name
```

## OpenAPI Server

The server to render pages.

### Generate Code Samples

Generate custom code samples for each API endpoint. Make sure to install the types package to give you type-safety when customising it:

```package-install
openapi-types -D
```

```ts
import { createOpenAPI } from 'fumadocs-openapi/server';

export const openapi = createOpenAPI({
  generateCodeSamples(endpoint) {
    return [
      {
        lang: 'js',
        label: 'JavaScript SDK',
        source: "console.log('hello')",
      },
    ];
  },
});
```

In addition, you can also specify code samples via OpenAPI schema.

```yaml
paths:
  /plants:
    get:
      x-codeSamples:
        - lang: js
          label: JavaScript SDK
          source: |
            const planter = require('planter');
            planter.list({ unwatered: true });
```

#### Disable Code Sample

You can disable the code sample for a specific language, for example, to disable cURL:

```ts
import { createOpenAPI } from 'fumadocs-openapi/server';

export const openapi = createOpenAPI({
  generateCodeSamples(endpoint) {
    return [
      {
        lang: 'curl',
        label: 'cURL',
        source: false,
      },
    ];
  },
});
```

### Renderer

Customise components in the page.

```ts
import { createOpenAPI } from 'fumadocs-openapi/server';

export const openapi = createOpenAPI({
  renderer: {
    Root(props) {
      // your own (server) component
    },
  },
});
```

## Advanced

### Using API Page

> This is not a public API, use it carefully.

To use the `APIPage` component in your MDX files:

```mdx
---
title: Delete Api
full: true
---

<APIPage
  document="./unkey.json"
  operations={[{ path: '/v1/apis.deleteApi', method: 'post' }]}
  hasHead={false}
/>
```

Unlike using the `generateFiles()` function, this supports revalidation of the OpenAPI schema if given an URL.

| Prop         | Description                               |
| ------------ | ----------------------------------------- |
| `document`   | OpenAPI Schema                            |
| `operations` | Operations (API endpoints) to be rendered |
| `hasHead`    | Enable to render the heading of operation |
`````

## File: apps/docs/content/docs/ui/(integrations)/openapi/index.mdx
`````
---
title: OpenAPI
description: Generating docs for OpenAPI schema
---

## Manual Setup

Install the required packages.

```package-install
fumadocs-openapi shiki
```

### Generate Styles

Please note that you must have Tailwind CSS v4 configured.

```css title="Tailwind CSS"
@import 'tailwindcss';
@import 'fumadocs-ui/css/neutral.css';
@import 'fumadocs-ui/css/preset.css';
/* [!code ++] */
@import 'fumadocs-openapi/css/preset.css';
```

### Configure Pages

Create an OpenAPI instance on the server. Fumadocs OpenAPI renders the pages on server-side.

```ts title="lib/source.ts"
import { createOpenAPI, attachFile } from 'fumadocs-openapi/server';
import { loader } from 'fumadocs-core/source';

export const source = loader({
  pageTree: {
    // [!code ++] adds a badge to each page item in page tree
    attachFile,
  },
});

// [!code ++]
export const openapi = createOpenAPI();
```

Add `APIPage` to your MDX Components, so that you can use it in MDX files.

```tsx title="mdx-components.tsx"
import defaultComponents from 'fumadocs-ui/mdx';
import { APIPage } from 'fumadocs-openapi/ui';
import { openapi } from '@/lib/source';
import type { MDXComponents } from 'mdx/types';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultComponents,
    APIPage: (props) => <APIPage {...openapi.getAPIPageProps(props)} />,
    ...components,
  };
}
```

> It is a React Server Component.

### Generate Files

You can generate MDX files directly from your OpenAPI schema.

Create a script:

```js title="scripts/generate-docs.mjs"
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  // the OpenAPI schema, you can also give it an external URL.
  input: ['./unkey.json'],
  output: './content/docs',
  // we recommend to enable it
  // make sure your endpoint description doesn't break MDX syntax.
  includeDescription: true,
});
```

> Only OpenAPI 3.0 and 3.1 are supported.

Generate docs with the script:

```bash
node ./scripts/generate-docs.mjs
```

## Features

The official OpenAPI integration supports:

- Basic API endpoint information
- Interactive API playground
- Example code to send request (in different programming languages)
- Response samples and TypeScript definitions
- Request parameters and body generated from schemas

### Demo

[View demo](/docs/openapi).
`````

## File: apps/docs/content/docs/ui/(integrations)/openapi/media-adapters.mdx
`````
---
title: Media Adapters
description: Support other media types
---

## Overview

A media adapter in Fumadocs supports:

- Converting value into `fetch()` body compatible with corresponding media type.
- Generate code example based on different programming language/tool.

Put your media adapters in a separate file.

```ts tab="lib/media-adapters.ts" twoslash
import type { MediaAdapter } from 'fumadocs-openapi';

export const myAdapter: MediaAdapter = {
  encode(data) {
    return JSON.stringify(data.body);
  },
  // returns code that inits a `body` variable, used for request body
  generateExample(data, ctx) {
    if (ctx.lang === 'js') {
      return `const body = "hello world"`;
    }

    if (ctx.lang === 'python') {
      return `body = "hello world"`;
    }

    if (ctx.lang === 'go' && 'addImport' in ctx) {
      ctx.addImport('strings');

      return `body := strings.NewReader("hello world")`;
    }
  },
};
```

```ts tab="lib/media-adapters.client.ts"
'use client';

// forward them so that Fumadocs can also use your media adapter in a client component
export { myAdapter } from './media-adapters';
```

Pass the adapter.

```ts title="lib/source.ts"
import { createOpenAPI } from 'fumadocs-openapi/server';
import * as Adapters from './media-adapters';
import * as ClientAdapters from './media-adapters.client';

export const openapi = createOpenAPI({
  proxyUrl: '/api/proxy',
  mediaAdapters: {
    // [!code ++:4] override the default adapter of `application/json`
    'application/json': {
      ...Adapters.myAdapter,
      client: ClientAdapters.myAdapter,
    },
  },
});
```
`````

## File: apps/docs/content/docs/ui/(integrations)/openapi/proxy.mdx
`````
---
title: Creating Proxy
description: Avoid CORS problem
---

## Introduction

A proxy server is useful for executing HTTP (`fetch`) requests, as it doesn't have CORS constraints like on the browser.
We can use it for executing HTTP requests on the OpenAPI playground, when the target API endpoints do not have CORS configured correctly.

<Callout type="warn" title="Warning">
  Do not use this on unreliable sites and API endpoints, the proxy server will
  forward all received headers & body, including HTTP-only `Cookies` and
  `Authorization` header.
</Callout>

### Setup

Create a route handler for proxy server.

```ts title="/api/proxy/route.ts"
import { openapi } from '@/lib/source';

export const { GET, HEAD, PUT, POST, PATCH, DELETE } = openapi.createProxy({
  // optional, we recommend to set a list of allowed origins for proxied requests
  allowedOrigins: ['https://example.com'],
});
```

> Follow the [Getting Started](/docs/ui/openapi) guide if `openapi` server is not yet configured.

And enable the proxy from `createOpenAPI`.

```ts title="lib/source.ts"
import { createOpenAPI } from 'fumadocs-openapi/server';

export const openapi = createOpenAPI({
  proxyUrl: '/api/proxy', // [!code ++]
});
```
`````

## File: apps/docs/content/docs/ui/(integrations)/feedback.mdx
`````
---
title: Feedback
description: Receive feedback from your users
---

## Overview

Feedback is crucial for knowing what your reader thinks, and help you to further improve documentation content.

## Installation

Add dependencies:

```package-install
class-variance-authority lucide-react
```

Copy the component:

<include cwd meta='title="components/rate.tsx"'>
  ./components/rate.tsx
</include>

The `@/lib/cn` import specifier may be different for your project, change it to import your `cn()` function if needed. (e.g. like `@/lib/utils`)

### How to Use

Now add the `<Rate />` component to your docs page:

```tsx
import { DocsPage } from 'fumadocs-ui/page';
import { Rate } from '@/components/rate';
import posthog from 'posthog-js';

export default async function Page() {
  return (
    <DocsPage toc={toc} full={page.data.full}>
      {/* at the bottom of page */}
      <Rate
        onRateAction={async (url, feedback) => {
          'use server';

          await posthog.capture('on_rate_docs', feedback);
        }}
      />
    </DocsPage>
  );
}
```

On above example, it reports user feedback by capturing a `on_rate_docs` event on PostHog.

You can specify your own server action to `onRateAction`, and report the feedback to different destinations like database, or GitHub Discussions via their API.

### Linking to GitHub Discussion

To report your feedback to GitHub Discussion, make a custom `onRateAction`.

You can copy this example as a starting point:

<include cwd meta="lib/github.ts">
  ./lib/github.ts
</include>

- Create your own GitHub App and obtain its app ID and private key.
- Fill required environment variables.
- Replace constants like `owner`, `repo`, and `DocsCategory`.
`````

## File: apps/docs/content/docs/ui/(integrations)/llms.mdx
`````
---
title: AI
description: Integrate AI functionality to Fumadocs.
---

## Docs for LLM

You can make your docs site more AI-friendly with dedicated docs content for large language models.

First, make a `getLLMText` function that converts pages into static MDX content:

<include meta='title="lib/get-llm-text.ts"'>./get-llm-text.ts</include>

> Modify it to include other remark plugins.

### `llms-full.txt`

A version of docs for AIs to read.

<include meta='title="app/llms-full.txt/route.ts"'>./llms.txt.ts</include>

### `*.mdx`

Allow people to append `.mdx` to a page to get its Markdown/MDX content.

You can make a route handler to return page content, and redirect users to that route using middleware.

<include meta='tab="app/llms.mdx/[[...slug]]/route.ts"'>./llms.mdx.ts</include>

```ts tab="next.config.ts"
import type { NextConfig } from 'next';

const config: NextConfig = {
  async rewrites() {
    return [
      {
        source: '/docs/:path*.mdx',
        destination: '/llms.mdx/:path*',
      },
    ];
  },
};
```

### Page Actions

Common page actions for AI, require `*.mdx` to be implemented first.

![AI Page Actions](/docs/ai-page-actions.png)

```npm
npx @fumadocs/cli add ai-page-actions
```

Use it in your docs page like:

```tsx title="app/docs/[[...slug]]/page.tsx"
<div className="flex flex-row gap-2 items-center border-b pt-2 pb-6">
  <LLMCopyButton markdownUrl={`${page.url}.mdx`} />
  <ViewOptions
    markdownUrl={`${page.url}.mdx`}
    githubUrl={`https://github.com/${owner}/${repo}/blob/dev/apps/docs/content/docs/${page.path}`}
  />
</div>
```

## AI Search

![AI Search](/docs/ai-search.png)

You can install the AI search dialog using Fumadocs CLI:

```package-install
npx @fumadocs/cli add ai-search
```

By default, it's configured for Inkeep AI. Since it's connected via Vercel AI SDK, you can connect to your own AI models easily.

> Note that Fumadocs doesn't provide the AI model, it's up to you.
`````

## File: apps/docs/content/docs/ui/(integrations)/open-graph.mdx
`````
---
title: Metadata
description: Usage with Next.js Metadata API
---

## Introduction

Next.js provides an useful set of utilities, allowing a flexible experience with Fumadocs.
Fumadocs uses the Next.js Metadata API for SEO.

Make sure to read their [Metadata section](https://nextjs.org/docs/app/building-your-application/optimizing/metadata) for the fundamentals of Metadata API.

## Open Graph Image

For docs pages, Fumadocs has a built-in metadata image generator.

You will need a route handler to get started.

<include cwd meta='title="app/docs-og/[...slug]/route.tsx"'>
  ../../examples/next-mdx/app/docs-og/[...slug]/route.tsx
</include>

> We need to append `image.png` to the end of slugs so that we can access it via `/docs-og/my-page/image.png`.

In your docs page, add the image to metadata.

```tsx title="app/docs/[[...slug]]/page.tsx"
import { notFound } from 'next/navigation';
import { source } from '@/lib/source';

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}) {
  const { slug = [] } = await params;
  const page = source.getPage(slug);
  if (!page) notFound();

  const image = ['/docs-og', ...slug, 'image.png'].join('/');
  return {
    title: page.data.title,
    description: page.data.description,
    openGraph: {
      images: image,
    },
    twitter: {
      card: 'summary_large_image',
      images: image,
    },
  };
}
```

### Font

You can also customise the font, options for Satori are also available on the built-in generator.

```ts
import { generateOGImage } from 'fumadocs-ui/og';

generateOGImage({
  fonts: [
    {
      name: 'Roboto',
      // Use `fs` (Node.js only) or `fetch` to read the font as Buffer/ArrayBuffer and provide `data` here.
      data: robotoArrayBuffer,
      weight: 400,
      style: 'normal',
    },
  ],
});
```
`````

## File: apps/docs/content/docs/ui/(integrations)/python.mdx
`````
---
title: Python
description: Generate docs from Python
---

<Callout type="warn" title="Experimental">
  Support for Python docgen is still experimental, please use it in caution.
</Callout>

## Setup

```package-install
fumadocs-python shiki
```

### Generate Docs

Install the Python command first, we need it to collect docs from your Python package.

```bash
pip install ./node_modules/fumadocs-python
```

Generate the docs as a JSON:

```bash
fumapy-generate your-package-name
# for example
fumapy-generate httpx
```

Use the following script to convert JSON into MDX:

```js title="scripts/generate-docs.mjs"
import { rimraf } from 'rimraf';
import * as Python from 'fumadocs-python';
import * as fs from 'node:fs/promises';

// output JSON file path
const jsonPath = './httpx.json';

async function generate() {
  const out = 'content/docs/(api)';
  // clean previous output
  await rimraf(out);

  const content = JSON.parse((await fs.readFile(jsonPath)).toString());
  const converted = Python.convert(content, {
    baseUrl: '/docs',
  });

  await Python.write(converted, {
    outDir: out,
  });
}

void generate();
```

<Callout type="warn" title="Be careful">
  While most docgens use Markdown or reStructuredText, Fumadocs uses **MDX**.
  Make sure your doc is valid in MDX syntax before running.
</Callout>

### MDX Components

Add the components.

```tsx
import defaultMdxComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';
import * as Python from 'fumadocs-python/components';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultMdxComponents,
    ...Python,
    ...components,
  };
}
```

Add styles:

```css title="Tailwind CSS"
@import 'tailwindcss';
@import 'fumadocs-ui/css/neutral.css';
@import 'fumadocs-ui/css/preset.css';
/* [!code ++] */
@import 'fumadocs-python/preset.css';
```
`````

## File: apps/docs/content/docs/ui/(integrations)/rss.mdx
`````
---
title: RSS
description: Generate a RSS feed for your docs/blog.
---

## Overview

You can implement the feed using a route handler like:

```ts title="app/rss.xml/route.ts"
import { Feed } from 'feed';
import { source } from '@/lib/source';
import { NextResponse } from 'next/server';

export const revalidate = false;

const baseUrl = 'https://fumadocs.dev';

export function GET() {
  const feed = new Feed({
    title: 'Fumadocs Blog',
    id: `${baseUrl}/blog`,
    link: `${baseUrl}/blog`,
    language: 'en',

    image: `${baseUrl}/banner.png`,
    favicon: `${baseUrl}/icon.png`,
    copyright: 'All rights reserved 2025, Fuma Nama',
  });

  for (const page of source.getPages().sort((a, b) => {
    return new Date(b.data.date).getTime() - new Date(a.data.date).getTime();
  })) {
    feed.addItem({
      id: page.url,
      title: page.data.title,
      description: page.data.description,
      link: `${baseUrl}${page.url}`,
      date: new Date(page.data.date),

      author: [
        {
          name: 'Fuma',
        },
      ],
    });
  }

  return new NextResponse(feed.rss2());
}
```

You can add an alternates object to the metadata object with your feed’s title and URL.

```ts title="app/layout.tsx"
import type { Metadata } from 'next';

export const metadata: Metadata = {
  alternates: {
    types: {
      'application/rss+xml': [
        {
          title: 'Fumadocs Blog',
          url: 'https://fumadocs.dev/blog/index.xml',
        },
      ],
    },
  },
};
```
`````

## File: apps/docs/content/docs/ui/(integrations)/typescript.mdx
`````
---
title: Typescript
description: Generate docs from Typescript definitions
---

## Usage

```package-install
fumadocs-typescript
```

### UI Integration

It comes with the `AutoTypeTable` component. Learn more about [Auto Type Table](/docs/ui/components/auto-type-table).

### MDX Integration

You can use it as a remark plugin:

```ts title="source.config.ts" tab="Fumadocs MDX"
import { remarkAutoTypeTable, createGenerator } from 'fumadocs-typescript';
import { defineConfig } from 'fumadocs-mdx/config';

const generator = createGenerator();

export default defineConfig({
  mdxOptions: {
    remarkPlugins: [[remarkAutoTypeTable, { generator }]],
  },
});
```

```ts tab="MDX Compiler"
import { remarkAutoTypeTable, createGenerator } from 'fumadocs-typescript';
import { compile } from '@mdx-js/mdx';

const generator = createGenerator();

await compile('...', {
  remarkPlugins: [[remarkAutoTypeTable, { generator }]],
});
```

It gives you a `auto-type-table` component.

You can use it like [Auto Type Table](/docs/ui/components/auto-type-table), but with additional rules:

- The value of attributes must be string.
- `path` accepts a path relative to the MDX file itself.
- You also need to add [`TypeTable`](/docs/ui/components/type-table) to MDX components.

```ts title="path/to/file.ts"
export interface MyInterface {
  name: string;
}
```

```mdx title="page.mdx"
<auto-type-table path="./path/to/file.ts" name="MyInterface" />
```

## Annotations

### Hide

Hide a field by adding `@internal` tsdoc tag.

```ts
interface MyInterface {
  /**
   * @internal
   */
  cache: number;
}
```

### Specify Type Name

You can specify the name of a type with the `@remarks` tsdoc tag.

```ts
interface MyInterface {
  /**
   * @remarks `timestamp` Returned by API. // [!code highlight]
   */
  time: number;
}
```

This will make the type of `time` property to be shown as `timestamp`.
`````

## File: apps/docs/content/docs/ui/components/accordion.mdx
`````
---
title: Accordion
description: Add Accordions to your documentation
preview: accordion
---

## Usage

Based on
[Radix UI Accordion](https://www.radix-ui.com/primitives/docs/components/accordion), useful for FAQ sections.

```mdx
import { Accordion, Accordions } from 'fumadocs-ui/components/accordion';

<Accordions type="single">
  <Accordion title="My Title">My Content</Accordion>
</Accordions>
```

### Accordions

<AutoTypeTable path="./content/docs/ui/props.ts" name="AccordionsProps" />

### Accordion

<AutoTypeTable path="./content/docs/ui/props.ts" name="AccordionProps" />

### Linking to Accordion

You can specify an `id` for accordion. The accordion will automatically open when the user is navigating to the page with the specified `id` in hash parameter.

```mdx
<Accordions>
<Accordion title="My Title" id="my-title">

My Content

</Accordion>
</Accordions>
```

> The value of accordion is same as title by default. When an id presents, it will be used as the value instead.
`````

## File: apps/docs/content/docs/ui/components/auto-type-table.mdx
`````
---
title: Auto Type Table
description: Auto-generated type table
---

<Wrapper>

<div className="bg-fd-background p-4 rounded-xl">

<AutoTypeTable name="AutoTypeTableExample" type={`export interface AutoTypeTableExample {
    /**
     * Markdown syntax like links, \`code\` are supported.
     *
     * See https://fumadocs.vercel.app/docs/ui/components/type-table
     */
    name: string;

    /**
    * We love Shiki.
    *
    * \`\`\`ts
    * console.log("Hello World, powered by Shiki");
    * \`\`\`
    */
    options: Partial<{ a: unknown }>;

}`} />

</div>

</Wrapper>

It generates a table for your docs based on TypeScript definitions.

## Usage

```package-install
fumadocs-typescript
```

Initialize the TypeScript compiler and add it as a MDX component.

```tsx title="mdx-components.tsx"
import defaultComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';
import { createGenerator } from 'fumadocs-typescript';
import { AutoTypeTable } from 'fumadocs-typescript/ui';

const generator = createGenerator();

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultComponents,
    AutoTypeTable: (props) => (
      <AutoTypeTable {...props} generator={generator} />
    ),
    ...components,
  };
}
```

### From File

It accepts a `path` prop that points to a typescript file, and `name` for the exported type name.

```ts title="path/to/file.ts"
export interface MyInterface {
  name: string;
}
```

```mdx
<AutoTypeTable path="./path/to/file.ts" name="MyInterface" />
```

The path is relative to your project directory (`cwd`), because `AutoTypeTable` is a React Server Component, it cannot access build-time information like MDX file path.

<Callout title="Server Component only" type="warn">

You cannot use this in a client component.

</Callout>

### From Type

You can specify the type to generate, without an actual TypeScript file.

```mdx
import { AutoTypeTable } from 'fumadocs-typescript/ui';

<AutoTypeTable type="{ hello: string }" />
```

When a `path` is given, it shares the same context as the TypeScript file.

```ts title="file.ts"
export type A = { hello: string };
```

```mdx
<AutoTypeTable path="file.ts" type="A & { world: string }" />
```

When `type` has multiple lines, the export statement and `name` prop are required.

```mdx
<AutoTypeTable
  path="file.ts"
  name="B"
  type={`
import { ReactNode } from "react"
export type B = ReactNode | { world: string }
`}
/>
```

### Functions

Notice that only object type is allowed. For functions, you should wrap them into an object instead.

```ts
export interface MyInterface {
  myFn: (input: string) => void;
}
```

### References

<auto-type-table path="../props.ts" name="AutoTypeTableProps" />

### File System

It relies on the file system, hence, the page referencing this component must be built in **build time**. Rendering the component on serverless runtime may cause problems.

### Deep Dive

Under the hood, it uses the [Typescript Compiler API](https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API) to extract type information.
Your `tsconfig.json` file in the current working directory will be loaded.

To change the compiler settings, pass a `options` prop to the component.

Learn more about [Typescript Docs Generation](/docs/ui/typescript).
`````

## File: apps/docs/content/docs/ui/components/banner.mdx
`````
---
title: Banner
description: Add a banner to your site
preview: banner
---

## Usage

Put the element at the top of your root layout, you can use it for displaying announcements.

```tsx
import { Banner } from 'fumadocs-ui/components/banner';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}): React.ReactElement {
  return (
    <html lang="en">
      <body>
        <Banner>Hello World</Banner>
        {children}
      </body>
    </html>
  );
}
```

### Variant

Change the default variant.

```tsx
import { Banner } from 'fumadocs-ui/components/banner';

<Banner variant="rainbow">Hello World</Banner>;

// customise colors
<Banner
  variant="rainbow"
  rainbowColors={[
    'rgba(255,100,0, 0.5)',
    'rgba(255,100,0, 0.5)',
    'transparent',
    'rgba(255,100,0, 0.5)',
    'transparent',
    'rgba(255,100,0, 0.5)',
    'transparent',
  ]}
>
  Hello World
</Banner>;
```

### Change Layout

By default, the banner uses a `style` tag to modify Fumadocs layouts (e.g. reduce the sidebar height).
You can disable it with:

```tsx
import { Banner } from 'fumadocs-ui/components/banner';

<Banner changeLayout={false}>Hello World</Banner>;
```

### Close

To allow users to close the banner, give the banner an ID.

```tsx
import { Banner } from 'fumadocs-ui/components/banner';

<Banner id="hello-world">Hello World</Banner>;
```

The state will be automatically persisted.
`````

## File: apps/docs/content/docs/ui/components/dynamic-codeblock.mdx
`````
---
title: Code Block (Dynamic)
description: A codeblock that also highlights code
preview: dynamicCodeBlock
---

## Usage

### Client Component

```tsx
import { DynamicCodeBlock } from 'fumadocs-ui/components/dynamic-codeblock';

<DynamicCodeBlock lang="ts" code='console.log("Hello World")' />;
```

Unlike the MDX [`CodeBlock`](/docs/ui/mdx/codeblock) component, this is a client component that can be used without MDX.
It highlights the code with Shiki and use the default component to render it.

Features:

- Can be pre-rendered on server
- load languages and themes on browser lazily

#### Options

```tsx
import { DynamicCodeBlock } from 'fumadocs-ui/components/dynamic-codeblock';

<DynamicCodeBlock
  lang="ts"
  code='console.log("Hello World")'
  options={{
    themes: {
      light: 'github-light',
      dark: 'github-dark',
    },
    components: {
      // override components (e.g. `pre` and `code`)
    },
    // other Shiki options
  }}
/>;
```

### Server Component

For a server component equivalent, you can use the built-in utility from core:

<include>./server-codeblock.tsx</include>
`````

## File: apps/docs/content/docs/ui/components/files.mdx
`````
---
title: Files
description: Display file structure in your documentation
preview: 'files'
---

## Usage

Wrap file components in `Files`.

```mdx
import { File, Folder, Files } from 'fumadocs-ui/components/files';

<Files>
  <Folder name="app" defaultOpen>
    <File name="layout.tsx" />
    <File name="page.tsx" />
    <File name="global.css" />
  </Folder>
  <Folder name="components">
    <File name="button.tsx" />
    <File name="tabs.tsx" />
    <File name="dialog.tsx" />
  </Folder>
  <File name="package.json" />
</Files>
```

### File

<AutoTypeTable path="./content/docs/ui/props.ts" name="FileProps" />

### Folder

<AutoTypeTable path="./content/docs/ui/props.ts" name="FolderProps" />
`````

## File: apps/docs/content/docs/ui/components/github-info.mdx
`````
---
title: GitHub Info
description: Display your GitHub repository information
preview: githubInfo
---

## Usage

```tsx
import { GithubInfo } from 'fumadocs-ui/components/github-info';

<GithubInfo
  owner="fuma-nama"
  repo="fumadocs"
  // your own GitHub access token (optional)
  token={process.env.GITHUB_TOKEN}
/>;
```

It's recommended to add it to your docs layout with `links` option:

```tsx title="app/docs/layout.tsx"
import { DocsLayout, type DocsLayoutProps } from 'fumadocs-ui/layouts/notebook';
import type { ReactNode } from 'react';
import { baseOptions } from '@/app/layout.config';
import { source } from '@/lib/source';
import { GithubInfo } from 'fumadocs-ui/components/github-info';

const docsOptions: DocsLayoutProps = {
  ...baseOptions,
  tree: source.pageTree,
  links: [
    {
      type: 'custom',
      children: (
        <GithubInfo owner="fuma-nama" repo="fumadocs" className="lg:-mx-2" />
      ),
    },
  ],
};

export default function Layout({ children }: { children: ReactNode }) {
  return <DocsLayout {...docsOptions}>{children}</DocsLayout>;
}
```
`````

## File: apps/docs/content/docs/ui/components/image-zoom.mdx
`````
---
title: Zoomable Image
description: Allow zoom-in images in your documentation
preview: zoomImage
---

## Usage

Replace `img` with `ImageZoom` in your MDX components.

```tsx title="mdx-components.tsx"
import { ImageZoom } from 'fumadocs-ui/components/image-zoom';
import defaultComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultComponents,
    img: (props) => <ImageZoom {...(props as any)} />,
    ...components,
  };
}
```

Now image zoom will be automatically enabled on all images.

```mdx
![Test](/banner.png)
```

### Image Optimization

A default [`sizes` property](https://nextjs.org/docs/app/api-reference/components/image#sizes) will be defined for Next.js `<Image />` component if not specified.
`````

## File: apps/docs/content/docs/ui/components/index.mdx
`````
---
title: Components
description: Additional components to improve your docs
index: true
---
`````

## File: apps/docs/content/docs/ui/components/inline-toc.mdx
`````
---
title: Inline TOC
description: Add Inline TOC into your documentation
preview: inlineTOC
---

## Usage

Pass TOC items to the component.

```mdx
import { InlineTOC } from 'fumadocs-ui/components/inline-toc';

<InlineTOC items={toc} />
```

### Use in Pages

You can add inline TOC into every page.

```tsx
<DocsPage>
  ...
  <InlineTOC items={toc} />
  ...
</DocsPage>
```

## Reference

<AutoTypeTable path="./content/docs/ui/props.ts" name="InlineTOCProps" />
`````

## File: apps/docs/content/docs/ui/components/steps.mdx
`````
---
title: Steps
description: Adding steps to your docs
preview: steps
---

## Usage

Put your steps into the `Steps` container.

```mdx
import { Step, Steps } from 'fumadocs-ui/components/steps';

<Steps>
<Step>

### Hello World

</Step>

<Step>

### Hello World

</Step>
</Steps>
```

> We recommend using Tailwind CSS utility classes directly on Tailwind CSS projects.

### Without imports

You can use the Tailwind CSS utilities without importing it.

```mdx
<div className="fd-steps">
  <div className="fd-step" />
</div>
```

It supports adding step styles to only headings with arbitrary variants.

```mdx
<div className='fd-steps [&_h3]:fd-step'>

### Hello World

</div>
```

<div className='fd-steps [&_h3]:fd-step'>

### Hello World

You no longer need to use the step component anymore.

</div>
`````

## File: apps/docs/content/docs/ui/components/tabs.mdx
`````
---
title: Tabs
description:
  A Tabs component built with Radix UI, with additional features such as
  persistent and shared value.
preview: tabs
---

## Usage

Add MDX components.

```tsx title="mdx-components.tsx"
import defaultMdxComponents from 'fumadocs-ui/mdx';
import * as TabsComponents from 'fumadocs-ui/components/tabs';
import type { MDXComponents } from 'mdx/types';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultMdxComponents,
    ...TabsComponents, // [!code ++]
    ...components,
  };
}
```

And use it like:

```mdx
<Tabs items={['Javascript', 'Rust']}>
  <Tab value="Javascript">Javascript is weird</Tab>
  <Tab value="Rust">Rust is fast</Tab>
</Tabs>
```

<Tabs items={['Javascript', 'Rust']}>
  <Tab value="Javascript">Javascript is weird</Tab>
  <Tab value="Rust">Rust is fast</Tab>
</Tabs>

### Without `value`

Without a `value`, it detects from the children index. Note that it might cause errors on re-renders, it's not encouraged if the tabs might change.

```mdx
import { Tab, Tabs } from 'fumadocs-ui/components/tabs';

<Tabs items={['Javascript', 'Rust']}>
  <Tab>Javascript is weird</Tab>
  <Tab>Rust is fast</Tab>
</Tabs>
```

<Tabs items={['Javascript', 'Rust']}>
  <Tab>Javascript is weird</Tab>
  <Tab>Rust is fast</Tab>
</Tabs>

### Shared Value

By passing an `groupId` property, you can share a value across all tabs with the same
id.

```mdx
<Tabs groupId="language" items={['Javascript', 'Rust']}>
  <Tab value="Javascript">Javascript is weird</Tab>
  <Tab value="Rust">Rust is fast</Tab>
</Tabs>
```

### Persistent

You can enable persistent by passing a `persist` property. The value will be
stored in `localStorage`, with its id as the key.

```mdx
<Tabs groupId="language" items={['Javascript', 'Rust']} persist>
  <Tab value="Javascript">Javascript is weird</Tab>
  <Tab value="Rust">Rust is fast</Tab>
</Tabs>
```

> Persistent only works if you have passed an `id`.

### Default Value

Set a default value by passing `defaultIndex`.

```mdx
<Tabs items={['Javascript', 'Rust']} defaultIndex={1}>
  <Tab value="Javascript">Javascript is weird</Tab>
  <Tab value="Rust">Rust is fast</Tab>
</Tabs>
```

### Link to Tab

Use HTML `id` attribute to link to a specific tab.

```mdx
<Tabs items={['Javascript', 'Rust', 'C++']}>
  <Tab value="Javascript">Javascript is weird</Tab>
  <Tab value="Rust">Rust is fast</Tab>
  <Tab id="tab-cpp" value="C++">
    `Hello World`
  </Tab>
</Tabs>
```

You can add the hash `#tab-cpp` to your URL and reload, the C++ tab will be activated.

<Tabs items={['Javascript', 'Rust', 'C++']}>
  <Tab value="Javascript">Javascript is weird</Tab>
  <Tab value="Rust">Rust is fast</Tab>
  <Tab id="tab-cpp" value="C++">
    `Hello World`
  </Tab>
</Tabs>

Additionally, the `updateAnchor` property can be set to `true` in the `Tabs` component
to automatically update the URL hash whenever time a new tab is selected:

```mdx
<Tabs items={['Javascript', 'Rust', 'C++']} updateAnchor>
  <Tab id="tab-js" value="Javascript">
    Javascript is weird
  </Tab>
  <Tab id="tab-rs" value="Rust">
    Rust is fast
  </Tab>
  <Tab id="tab-cpp" value="C++">
    `Hello World`
  </Tab>
</Tabs>
```

<UrlBar />

<Tabs items={['Hello', 'World']} updateAnchor>
  <Tab id="tab-hello" value="Hello">
    Hello!
  </Tab>
  <Tab id="tab-world" value="World">
    World!
  </Tab>
</Tabs>

## Advanced Usage

Use it in the Radix UI primitive way, see [Radix UI](https://radix-ui.com/primitives/docs/components/tabs) for more details.

```mdx
<Tabs defaultValue="npm">
  <TabsList>
    <TabsTrigger value="npm">
      <NpmIcon />
      npm
    </TabsTrigger>
  </TabsList>
  <TabsContent value="npm">Hello World</TabsContent>
</Tabs>
```

<Tabs defaultValue="npm">
  <TabsList>
    <TabsTrigger value="npm">
      <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <title>npm</title>
        <path
          fill="currentColor"
          d="M1.763 0C.786 0 0 .786 0 1.763v20.474C0 23.214.786 24 1.763 24h20.474c.977 0 1.763-.786 1.763-1.763V1.763C24 .786 23.214 0 22.237 0zM5.13 5.323l13.837.019-.009 13.836h-3.464l.01-10.382h-3.456L12.04 19.17H5.113z"
        />
      </svg>
      npm
    </TabsTrigger>
  </TabsList>
  <TabsContent value="npm">Hello World</TabsContent>
</Tabs>
`````

## File: apps/docs/content/docs/ui/components/type-table.mdx
`````
---
title: Type Table
description: A table for documenting types
preview: typeTable
---

## Usage

It accepts a `type` property.

```mdx
import { TypeTable } from 'fumadocs-ui/components/type-table';

<TypeTable
  type={{
    percentage: {
      description:
        'The percentage of scroll position to display the roll button',
      type: 'number',
      default: 0.2,
    },
  }}
/>
```

## References

### Type Table

<AutoTypeTable path="./content/docs/ui/props.ts" name="TypeTableProps" />

### Object Type

<AutoTypeTable path="./content/docs/ui/props.ts" name="ObjectTypeProps" />
`````

## File: apps/docs/content/docs/ui/layouts/docs.mdx
`````
---
title: Docs Layout
description: The layout of documentation
---

The layout of documentation pages, it includes a sidebar and mobile-only navbar.

> It is a server component, you should not reference it in a client component.

## Usage

Pass your page tree to the component.

```tsx title="layout.tsx"
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import { baseOptions } from '@/app/layout.config';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout {...baseOptions} tree={tree}>
      {children}
    </DocsLayout>
  );
}
```

<AutoTypeTable
  path="./content/docs/ui/props.ts"
  type="Omit<DocsLayoutProps, 'children' | 'disableThemeSwitch'>"
/>

## Sidebar

```tsx title="layout.tsx"
import { DocsLayout } from 'fumadocs-ui/layouts/docs';

<DocsLayout
  sidebar={{
    enabled: true,
    // replace the default sidebar
    // component:
  }}
/>;
```

> See [Sidebar Links](/docs/ui/navigation/sidebar) for customising sidebar items.

<AutoTypeTable path="./content/docs/ui/props.ts" name="SidebarProps" />

## Nav

A mobile-only navbar, we recommend to customise it from `baseOptions`.

<div className='max-w-[460px] mx-auto'>

![Docs Nav](/docs/docs-nav.png)

</div>

```tsx
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export const baseOptions: BaseLayoutProps = {
  githubUrl: 'https://github.com/fuma-nama/fumadocs',
  nav: {
    title: 'My App',
  },
};
```

<AutoTypeTable
  path="./content/docs/ui/props.ts"
  type="Omit<NavbarProps, 'children'>"
/>

### Transparent Mode

To make the navbar background transparent, you can configure transparent mode.

```tsx
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export const baseOptions: BaseLayoutProps = {
  nav: {
    transparentMode: 'top',
  },
};
```

| Mode     | Description                              |
| -------- | ---------------------------------------- |
| `always` | Always use a transparent background      |
| `top`    | When at the top of page                  |
| `none`   | Disable transparent background (default) |

### Replace Navbar

To replace the navbar in Docs Layout, set `nav.component` to your own component.

```tsx title="layout.tsx"
import { baseOptions } from '@/app/layout.config';
import { DocsLayout } from 'fumadocs-ui/layouts/notebook';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout
      {...baseOptions}
      nav={{
        component: <CustomNavbar />,
      }}
    >
      {children}
    </DocsLayout>
  );
}
```

Fumadocs uses **CSS Variables** to share the size of layout components, and fit each layout component into appropriate position.

You need to override `--fd-nav-height` to the exact height of your custom navbar, this can be done with a CSS stylesheet (e.g. in `global.css`):

```css
:root {
  --fd-nav-height: 80px !important;
}
```

## Advanced

### Disable Prefetching

By default, it uses the Next.js Link component with prefetch enabled.
When the link component appears into the browser viewport, the content (RSC payload) will be prefetched.

On Vercel, this may cause a high usage of serverless functions and Data Cache.
It can also hit the limits of some other hosting platforms.

You can disable prefetching to reduce the amount of RSC requests.

```tsx
import { DocsLayout } from 'fumadocs-ui/layouts/docs';

<DocsLayout sidebar={{ prefetch: false }} />;
```
`````

## File: apps/docs/content/docs/ui/layouts/home-layout.mdx
`````
---
title: Home Layout
description: Shared layout for other pages
---

## Usage

Add a navbar and search dialog across other pages.

```tsx title="/app/(home)/layout.tsx"
import { HomeLayout } from 'fumadocs-ui/layouts/home';
import { baseOptions } from '@/app/layout.config';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return <HomeLayout {...baseOptions}>{children}</HomeLayout>;
}
```

Create a [Route Group](https://nextjs.org/docs/app/building-your-application/routing/route-groups) to share the same layout across multiple pages.

<Files>
  <Folder name="(home)" defaultOpen>
    <File name="page.tsx" />
    <File name="layout.tsx" />
  </Folder>
  <Folder name="/docs">
    <Folder name={'[[..slugs]]'}>
      <File name="page.tsx" />
    </Folder>
    <File name="layout.tsx" />
  </Folder>
</Files>

We recommend to customise it from [`baseOptions`](/docs/ui/navigation/links).
`````

## File: apps/docs/content/docs/ui/layouts/notebook.mdx
`````
---
title: Notebook
description: A more compact version of Docs Layout
---

![Notebook](/docs/notebook.png)

## Usage

Enable the notebook layout with `fumadocs-ui/layouts/notebook`, it's a more compact layout than the default one.

```tsx title="layout.tsx"
import { DocsLayout } from 'fumadocs-ui/layouts/notebook'; // [!code highlight]
import { baseOptions } from '@/app/layout.config';
import { source } from '@/lib/source';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout {...baseOptions} tree={source.pageTree}>
      {children}
    </DocsLayout>
  );
}
```

## Configurations

The options are inherited from [Docs Layout](/docs/ui/layouts/docs), with minor differences:

- sidebar/navbar cannot be replaced, Notebook layout is more opinionated than the default one.
- additional options (see below).

### Tab Mode

Configure the style of sidebar tabs.

![Notebook](/docs/notebook-tab-mode.png)

```tsx title="layout.tsx"
import { DocsLayout } from 'fumadocs-ui/layouts/notebook';
import { baseOptions } from '@/app/layout.config';
import { source } from '@/lib/source';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout
      {...baseOptions}
      tabMode="navbar" // [!code ++]
      tree={source.pageTree}
    >
      {children}
    </DocsLayout>
  );
}
```

### Nav Mode

Configure the style of navbar.

![Notebook](/docs/notebook-nav-mode.png)

```tsx title="layout.tsx"
import { DocsLayout } from 'fumadocs-ui/layouts/notebook';
import { baseOptions } from '@/app/layout.config';
import { source } from '@/lib/source';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout
      {...baseOptions}
      nav={{ ...baseOptions.nav, mode: 'top' }} // [!code ++]
      tree={source.pageTree}
    >
      {children}
    </DocsLayout>
  );
}
```
`````

## File: apps/docs/content/docs/ui/layouts/page.mdx
`````
---
title: Docs Page
description: A page in your documentation
---

Page is the base element of a documentation, it includes Table of contents,
Footer, and Breadcrumb.

## Usage

```tsx title="page.tsx"
import {
  DocsPage,
  DocsDescription,
  DocsTitle,
  DocsBody,
} from 'fumadocs-ui/page';

<DocsPage>
  <DocsTitle>title</DocsTitle>
  <DocsDescription>description</DocsDescription>
  <DocsBody>
    <h2>This heading looks good!</h2>
    It applies the Typography styles, wrap your content here.
  </DocsBody>
</DocsPage>;
```

<Callout type='info' title='Good to know'>

Instead of rendering the title with `DocsTitle` in `page.tsx`, you can put the title into MDX file.
This will render the title in the MDX body.

</Callout>

### Edit on GitHub

You can also add your own component.

```tsx
import { DocsBody } from 'fumadocs-ui/page';

<DocsBody>
  <a
    href={`https://github.com/fuma-nama/fumadocs/blob/main/content/docs/${page.path}`}
    rel="noreferrer noopener"
    target="_blank"
    className="w-fit border rounded-xl p-2 font-medium text-sm text-fd-secondary-foreground bg-fd-secondary transition-colors hover:text-fd-accent-foreground hover:bg-fd-accent"
  >
    Edit on GitHub
  </a>
</DocsBody>;
```

## Configurations

### Full Mode

To extend the page to fill up all available space, pass `full` to the page component.
This will force TOC to be shown as a popover.

```tsx
import { DocsPage } from 'fumadocs-ui/page';

<DocsPage full>...</DocsPage>;
```

### Table of Contents

An overview of all the headings in your article, it requires an array of headings.

For Markdown and MDX documents, You can obtain it using the
[TOC Utility](/docs/headless/utils/get-toc). Content sources like Fumadocs MDX offer this out-of-the-box.

```tsx
import { DocsPage } from 'fumadocs-ui/page';

<DocsPage toc={headings}>...</DocsPage>;
```

You can customise or disable it with the `tableOfContent` option, or with `tableOfContentPopover` on smaller devices.

```tsx
import { DocsPage } from 'fumadocs-ui/page';

<DocsPage tableOfContent={options} tableOfContentPopover={options}>
  ...
</DocsPage>;
```

<AutoTypeTable path="./content/docs/ui/props.ts" name="TOCProps" />

#### Style

You can choose another style for TOC, like `clerk` inspired by https://clerk.com:

```tsx
import { DocsPage } from 'fumadocs-ui/page';

<DocsPage
  tableOfContent={{
    style: 'clerk',
  }}
>
  ...
</DocsPage>;
```

### Last Updated Time

Display last updated time of the page.

```tsx
import { DocsPage } from 'fumadocs-ui/page';

<DocsPage lastUpdate={new Date(lastModifiedTime)} />;
```

Since you might use different version controls (e.g. Github) or CMS like Sanity, Fumadocs UI doesn't display the last updated time by
default.

<Tabs items={['Fumadocs MDX', 'GitHub API']}>

    <Tab>

You can enable [`lastModifiedTime`](/docs/mdx/last-modified).

```tsx
import { DocsPage } from 'fumadocs-ui/page';
import { source } from '@/lib/source';
const page = source.getPage(['...']);

<DocsPage lastUpdate={new Date(page.data.lastModified)} />;
```

    </Tab>

    <Tab>

For Github hosted documents, you can use
the [`getGithubLastEdit`](/docs/headless/utils/git-last-edit) utility.

```tsx
import { DocsPage } from 'fumadocs-ui/page';
import { getGithubLastEdit } from 'fumadocs-core/server';

const time = await getGithubLastEdit({
  owner: 'fuma-nama',
  repo: 'fumadocs',
  path: `content/docs/${page.path}`,
});

<DocsPage lastUpdate={new Date(time)} />;
```

    </Tab>

</Tabs>

### Footer

Footer is a navigation element that has two buttons to jump to the next and previous pages. When not specified, it shows the neighbour pages found from page tree.

Customise the footer with the `footer` option.

```tsx
import { DocsPage, DocsBody } from 'fumadocs-ui/page';

<DocsPage footer={options}>
  <DocsBody>...</DocsBody>
</DocsPage>;
```

<AutoTypeTable path="./content/docs/ui/props.ts" name="FooterProps" />

### Breadcrumb

A navigation element, shown only when user is navigating in folders.

<AutoTypeTable path="./content/docs/ui/props.ts" name="BreadcrumbProps" />
`````

## File: apps/docs/content/docs/ui/layouts/root-provider.mdx
`````
---
title: Root Provider
description: The context provider of Fumadocs UI.
---

The context provider of all the components, including `next-themes` and context
for search dialog. It should be located at the root layout.

## Usage

```jsx
import { RootProvider } from 'fumadocs-ui/provider';

export default function Layout({ children }) {
  return (
    <html lang="en">
      <body>
        <RootProvider>{children}</RootProvider>
      </body>
    </html>
  );
}
```

### Search Dialog

Customize or disable the search dialog with `search` option.

```jsx
<RootProvider
  search={{
    enabled: false,
  }}
>
  {children}
</RootProvider>
```

Learn more from [Search](/docs/ui/search).

### Theme Provider

Fumadocs supports light/dark modes with [`next-themes`](https://github.com/pacocoursey/next-themes).
Customise or disable it with `theme` option.

```jsx
<RootProvider
  theme={{
    enabled: false,
  }}
>
  {children}
</RootProvider>
```
`````

## File: apps/docs/content/docs/ui/markdown/index.mdx
`````
---
title: Markdown
description: How to write documents
---

## Introduction

Fumadocs provides many useful extensions to MDX, a markup language. Here is a brief introduction to the default MDX syntax of Fumadocs.

> MDX is not the only supported format of Fumadocs. In fact, you can use any renderers such as `next-mdx-remote` or CMS.

## MDX

We recommend MDX, a superset of Markdown with JSX syntax.
It allows you to import components, and use them in the document, or even writing JavaScript.

See:

- [MDX Syntax](https://mdxjs.com/docs/what-is-mdx/#mdx-syntax).
- GFM (GitHub Flavored Markdown) is also supported, see [GFM Specification](https://github.github.com/gfm).

```mdx
---
title: This is a document
---

import { Component } from './component';

<Component name="Hello" />

# Heading

## Heading

### Heading

#### Heading

Hello World, **Bold**, _Italic_, ~~Hidden~~

1. First
2. Second
3. Third

- Item 1
- Item 2

> Quote here

![alt](/image.png)

| Table | Description |
| ----- | ----------- |
| Hello | World       |
```

Images are automatically optimized for `next/image`.

### Auto Links

Internal links use the `next/link` component to allow prefetching and avoid hard-reload.

External links will get the default `rel="noreferrer noopener" target="_blank"` attributes for security.

```mdx
[My Link](https://github.github.com/gfm)

This also works: https://github.github.com/gfm.
```

### Cards

Useful for adding links.

```mdx
import { HomeIcon } from 'lucide-react';

<Cards>
  <Card
    href="https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating"
    title="Fetching, Caching, and Revalidating"
  >
    Learn more about caching in Next.js
  </Card>
  <Card title="href is optional">Learn more about `fetch` in Next.js.</Card>
  <Card icon={<HomeIcon />} href="/" title="Home">
    You can include icons too.
  </Card>
</Cards>
```

<Cards>
  <Card
    href="https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating"
    title="Fetching, Caching, and Revalidating"
  >
    Learn more about caching in Next.js
  </Card>
  <Card title="href is optional">Learn more about `fetch` in Next.js.</Card>
  <Card icon={<HomeIcon />} href="/" title="Home">
    You can include icons too.
  </Card>
</Cards>

#### "Further Reading" Section

You can do something like:

```tsx title="page.tsx"
import { getPageTreePeers } from 'fumadocs-core/server';
import { source } from '@/lib/source';

<Cards>
  {getPageTreePeers(source.pageTree, '/docs/my-page').map((peer) => (
    <Card key={peer.url} title={peer.name} href={peer.url}>
      {peer.description}
    </Card>
  ))}
</Cards>;
```

This will show the other pages in the same folder as cards.

<DocsCategory url="/docs/ui/navigation" />

### Callouts

Useful for adding tips/warnings, it is included by default. You can specify the type of callout:

- `info` (default)
- `warn`/`warning`
- `error`
- `success`

```mdx
<Callout>Hello World</Callout>

<Callout title="Title">Hello World</Callout>

<Callout title="Title" type="error">
  Hello World
</Callout>
```

<Callout>Hello World</Callout>

<Callout title="Title" type="warn">
  Hello World
</Callout>

<Callout title="Title" type="error">
  Hello World
</Callout>

### Headings

An anchor is automatically applied to each heading, it sanitizes invalid characters like spaces. (e.g. `Hello World` to `hello-world`)

```md
# Hello `World`
```

#### TOC Settings

The table of contents (TOC) will be generated based on headings, you can also customise the effects of headings:

```md
# Heading [!toc]

This heading will be hidden from TOC.

# Another Heading [toc]

This heading will **only** be visible in TOC, you can use it to add additional TOC items.
Like headings rendered in a React component:

<MyComp />
```

#### Custom Anchor

You can add `[#slug]` to customise heading anchors.

```md
# heading [#my-heading-id]
```

You can also chain it with TOC settings like:

```md
# heading [toc] [#my-heading-id]
```

To link people to a specific heading, add the heading id to hash fragment: `/page#my-heading-id`.

### Codeblock

Syntax Highlighting is supported by default using [Rehype Code](/docs/headless/mdx/rehype-code).

````mdx
```js
console.log('Hello World');
```

```js title="My Title"
console.log('Hello World');
```
````

#### Line Numbers

Show line numbers, it also works with Twoslash and other transformers.

````mdx tab="Input"
```ts twoslash lineNumbers
const a = 'Hello World';
//    ^?
console.log(a); // [!code highlight]
```
````

```ts twoslash lineNumbers tab="Output"
const a = 'Hello World';
//    ^?
console.log(a); // [!code highlight]
```

You can set the initial value of line numbers.

````mdx tab="Input"
```js lineNumbers=4
function main() {
  console.log('starts from 4');

  return 0;
}
```
````

```js lineNumbers=4 tab="Output"
function main() {
  console.log('starts from 4');

  return 0;
}
```

#### Shiki Transformers

We support some of the [Shiki Transformers](https://shiki.style/packages/transformers), allowing you to highlight/style specific lines.

````md tab="Input"
```tsx
// highlight a line
<div>Hello World</div> // [\!code highlight]

// highlight a word
// [\!code word:Fumadocs]
<div>Fumadocs</div>

// diff styles
console.log('hewwo'); // [\!code --]
console.log('hello'); // [\!code ++]

// focus
return new ResizeObserver(() => {}) // [\!code focus]
```
````

```tsx tab="Output"
// highlight a line
<div>Hello World</div> // [!code highlight]

// highlight a word
// [!code word:Fumadocs]
<div>Fumadocs</div>

// diff styles:
console.log('hewwo'); // [!code --]
console.log('hello'); // [!code ++]

// focus
return new ResizeObserver(() => {}) // [!code focus]
```

#### Tab Groups

````mdx
```ts tab="Tab 1"
console.log('A');
```

```ts tab="Tab 2"
console.log('B');
```
````

```ts tab="Tab 1"
console.log('A');
```

```ts tab="Tab 2"
console.log('B');
```

While disabled by default, you use MDX in tab values by configuring the remark plugin:

```ts tab="Fumadocs MDX" title="source.config.ts"
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    remarkCodeTabOptions: {
      parseMdx: true, // [!code ++]
    },
  },
});
```

```ts tab="MDX Compiler"
import { compile } from '@mdx-js/mdx';
import { remarkCodeTab } from 'fumadocs-core/mdx-plugins';

await compile('...', {
  remarkPlugins: [
    [
      remarkCodeTab,
      {
        parseMdx: true, // [!code ++]
      },
    ],
  ],
});
```

````mdx
```ts tab="<Building /> Tab 1"
console.log('A');
```

```ts tab="<Rocket /> Tab 2"
console.log('B');
```
````

```ts tab="<Building /> Tab 1"
console.log('A');
```

```ts tab="<Rocket /> Tab 2"
console.log('B');
```

### Include

> This is only available on **Fumadocs MDX**.

Reference another file (can also be a Markdown/MDX document).
Specify the target file path in `<include>` tag (relative to the MDX file itself).

```mdx title="page.mdx"
<include>./another.mdx</include>
```

See [other usages of include](/docs/mdx/include).

### NPM Commands

Useful for generating commands for installing packages with different package managers.

````md tab="Input"
```npm
npm i next -D
```
````

```npm tab="Output"
npm i next -D
```

When using Fumadocs MDX, you can customise it like:

```tsx title="source.config.ts"
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    remarkNpmOptions: {
      // ...
    },
  },
});
```

### Other Components

You can configure & use the [built-in components](/docs/ui/components) in your MDX document, such as Tabs, Accordions and Zoomable Image.

## Additional Features

You may be interested:

<DocsCategory />
`````

## File: apps/docs/content/docs/ui/markdown/math.mdx
`````
---
title: Math
description: Writing math equations in Markdown/MDX.
---

## Getting Started

```package-install
remark-math rehype-katex katex
```

### Add Plugins

Add the required remark/rehype plugins, the code might be vary depending on your content source.

```ts title="source.config.ts" tab="Fumadocs MDX"
import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math';
import { defineConfig } from 'fumadocs-mdx/config';

export default defineConfig({
  mdxOptions: {
    remarkPlugins: [remarkMath],
    // Place it at first, it should be executed before the syntax highlighter
    rehypePlugins: (v) => [rehypeKatex, ...v],
  },
});
```

### Add Stylesheet

Add the following to root layout to make it looks great:

```tsx title="layout.tsx"
import 'katex/dist/katex.css';
```

### Done

Type some TeX expression in your documents, like the Pythagoras theorem:

````mdx
Inline: $$c = \pm\sqrt{a^2 + b^2}$$

```math
c = \pm\sqrt{a^2 + b^2}
```
````

Inline: $$c = \pm\sqrt{a^2 + b^2}$$

```math
c = \pm\sqrt{a^2 + b^2}
```

Taylor Expansion (expressing holomorphic function $$f(x)$$ in power series):

```math
\displaystyle {\begin{aligned}T_{f}(z)&=\sum _{k=0}^{\infty }{\frac {(z-c)^{k}}{2\pi i}}\int _{\gamma }{\frac {f(w)}{(w-c)^{k+1}}}\,dw\\&={\frac {1}{2\pi i}}\int _{\gamma }{\frac {f(w)}{w-c}}\sum _{k=0}^{\infty }\left({\frac {z-c}{w-c}}\right)^{k}\,dw\\&={\frac {1}{2\pi i}}\int _{\gamma }{\frac {f(w)}{w-c}}\left({\frac {1}{1-{\frac {z-c}{w-c}}}}\right)\,dw\\&={\frac {1}{2\pi i}}\int _{\gamma }{\frac {f(w)}{w-z}}\,dw=f(z),\end{aligned}}
```

<Callout title="Tip">

    You can actually copy equations on Wikipedia, they will be converted into a KaTeX string when you paste it.

```math
\displaystyle S[{\boldsymbol {q}}]=\int _{a}^{b}L(t,{\boldsymbol {q}}(t),{\dot {\boldsymbol {q}}}(t))\,dt.
```

</Callout>
`````

## File: apps/docs/content/docs/ui/markdown/mermaid.mdx
`````
---
title: Mermaid
description: Rendering diagrams in your docs
---

Fumadocs doesn't have a built-in Mermaid wrapper provided, we recommend using `mermaid` directly.

## Setup

Install the required dependencies, `next-themes` is used with Fumadocs to manage the light/dark mode.

```package-install
mermaid next-themes
```

Create the Mermaid component:

<include cwd meta='title="components/mdx/mermaid.tsx"'>
  ./components/mdx/mermaid.tsx
</include>

> This is originally inspired by [remark-mermaid](https://github.com/the-guild-org/docs/blob/main/packages/remark-mermaid/src/mermaid.tsx).

Add the component as a MDX component:

```tsx title="mdx-components.tsx"
import defaultMdxComponents from 'fumadocs-ui/mdx';
import { Mermaid } from '@/components/mdx/mermaid';
import type { MDXComponents } from 'mdx/types';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultMdxComponents,
    Mermaid,
    ...components,
  };
}
```

## Usage

Use it in MDX files.

```mdx
<Mermaid
  chart="
graph TD;
subgraph AA [Consumers]
A[Mobile app];
B[Web app];
C[Node.js client];
end
subgraph BB [Services]
E[REST API];
F[GraphQL API];
G[SOAP API];
end
Z[GraphQL API];
A --> Z;
B --> Z;
C --> Z;
Z --> E;
Z --> F;
Z --> G;"
/>
```

<Tabs items={['Diagram', 'User Journey']}>

    <Tab>
    <Mermaid
        chart="

graph TD;
subgraph AA [Consumers]
A[Mobile app];
B[Web app];
C[Node.js client];
end
subgraph BB [Services]
E[REST API];
F[GraphQL API];
G[SOAP API];
end
Z[GraphQL API];
A --> Z;
B --> Z;
C --> Z;
Z --> E;
Z --> F;
Z --> G;"
/>

</Tab>

    <Tab>
        <Mermaid
            chart="

journey
title My working day
section Go to work
Make tea: 5: Me
Go upstairs: 3: Me
Do work: 1: Me, Cat
section Go home
Go downstairs: 5: Me
Sit down: 5: Me
"
/>

    </Tab>

</Tabs>
`````

## File: apps/docs/content/docs/ui/markdown/twoslash.mdx
`````
---
title: Twoslash
description: Use Typescript Twoslash in your docs
---

## Usage

Thanks to the Twoslash integration of [Shiki](https://github.com/shikijs/shiki), the default code syntax highlighter, it is as simple as adding a transformer.

```package-install
fumadocs-twoslash twoslash
```

Update your `serverExternalPackages` in Next.js config:

```js
import { createMDX } from 'fumadocs-mdx/next';

const config = {
  reactStrictMode: true,
  serverExternalPackages: ['typescript', 'twoslash'],
};

const withMDX = createMDX();

export default withMDX(config);
```

Add to your Shiki transformers.

```ts twoslash title="source.config.ts (Fumadocs MDX)"
import { defineConfig } from 'fumadocs-mdx/config';
import { transformerTwoslash } from 'fumadocs-twoslash';
import { rehypeCodeDefaultOptions } from 'fumadocs-core/mdx-plugins';

export default defineConfig({
  mdxOptions: {
    rehypeCodeOptions: {
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
      transformers: [
        ...(rehypeCodeDefaultOptions.transformers ?? []),
        transformerTwoslash(),
      ],
    },
  },
});
```

Add styles, Tailwind CSS v4 is required.

```css title="Tailwind CSS"
@import 'fumadocs-twoslash/twoslash.css';
```

Add MDX components.

```tsx title="mdx-components.tsx"
import * as Twoslash from 'fumadocs-twoslash/ui';
import defaultComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultComponents,
    ...Twoslash,
    ...components,
  };
}
```

Now you can add `twoslash` meta string to codeblocks.

````md
```ts twoslash
console.log('Hello World');
```
````

### Example

Learn more about [Twoslash notations](https://twoslash.netlify.app/refs/notations).

```ts twoslash title="Test" lineNumbers
type Player = {
  /**
   * The player name
   * @default 'user'
   */
  name: string;
};

// ---cut---
// @noErrors
console.g;
//       ^|

const player: Player = { name: 'Hello World' };
//    ^?
```

```ts twoslash
const a = '123';

console.log(a);
//      ^^^
```

```ts twoslash
import { generateFiles } from 'fumadocs-openapi';

void generateFiles({
  input: ['./museum.yaml'],
  output: './content/docs/ui',
});
```

```ts twoslash
// @errors: 2588
const a = '123';

a = 132;
```

## Cache

You can enable filesystem cache with `typesCache` option:

```ts twoslash title="source.config.ts"
import { transformerTwoslash } from 'fumadocs-twoslash';
import { createFileSystemTypesCache } from 'fumadocs-twoslash/cache-fs';

transformerTwoslash({
  typesCache: createFileSystemTypesCache(),
});
```
`````

## File: apps/docs/content/docs/ui/mdx/codeblock.mdx
`````
---
title: Code Block
description: Displaying Shiki highlighted code blocks
---

<Wrapper>
<div className="bg-fd-background rounded-lg prose-no-margin">

```js title="config.js"
import createMDX from 'fumadocs-mdx/config';

const withMDX = createMDX();

// [!code word:config]
/** @type {import('next').NextConfig} */
const config = {
  // [!code highlight]
  reactStrictMode: true, // [!code highlight]
}; // [!code highlight]

export default withMDX(config);
```

</div>
</Wrapper>

This is a MDX component to be used with [Rehype Code](/docs/headless/mdx/rehype-code) to display highlighted codeblocks.

Supported features:

- Copy button
- Custom titles and icons

> If you're looking for an equivalent with runtime syntax highlighting, see [Dynamic Code Block](/docs/ui/components/dynamic-codeblock).

## Usage

Wrap the pre element in `<CodeBlock />`, which acts as the wrapper of code block.

```tsx title="mdx-components.tsx"
import defaultComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';
import { CodeBlock, Pre } from 'fumadocs-ui/components/codeblock';

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultComponents,
    // HTML `ref` attribute conflicts with `forwardRef`
    pre: ({ ref: _ref, ...props }) => (
      <CodeBlock {...props}>
        <Pre>{props.children}</Pre> {/* [!code highlight] */}
      </CodeBlock>
    ),
    ...components,
  };
}
```

See [Markdown](/docs/ui/markdown#codeblock) for usages.

### Keep Background

Use the background color generated by Shiki.

```tsx
import { Pre, CodeBlock } from 'fumadocs-ui/components/codeblock';

<CodeBlock keepBackground {...props}>
  <Pre>{props.children}</Pre>
</CodeBlock>;
```

### Icons

Specify a custom icon by passing an `icon` prop to `CodeBlock` component.

By default, the icon will be injected by the custom Shiki transformer.

```js title="config.js"
console.log('js');
```
`````

## File: apps/docs/content/docs/ui/mdx/index.mdx
`````
---
title: MDX
description: Default MDX Components
---

## Usage

The default MDX components include Cards, Callouts, Code Blocks and Headings.

```ts
import defaultMdxComponents from 'fumadocs-ui/mdx';
```

### Relative Link

To support links with relative file path in `href`, override the default `a` component with:

```tsx title="app/docs/[[...slug]]/page.tsx"
import { createRelativeLink } from 'fumadocs-ui/mdx';
import { source } from '@/lib/source';
import { getMDXComponents } from '@/mdx-components';

const page = source.getPage(['...']);

return (
  <MdxContent
    components={getMDXComponents({
      // override the `a` tag
      a: createRelativeLink(source, page),
    })}
  />
);
```

```mdx
[My Link](./file.mdx)
```

[Example: `../(integrations)/open-graph.mdx`](<../(integrations)/open-graph.mdx>)

<Callout type="warn">Server Component only.</Callout>
`````

## File: apps/docs/content/docs/ui/navigation/index.mdx
`````
---
title: Navigation
description: Configure navigation in your Fumadocs app.
index: true
---
`````

## File: apps/docs/content/docs/ui/navigation/links.mdx
`````
---
title: Layout Links
description: Customise the shared navigation links on all layouts.
---

## Overview

Fumadocs allows adding additional links to your layouts with a `links` prop, like linking to your "showcase" page.

<div className="not-prose grid gap-2 *:border max-sm:*:last:hidden sm:grid-cols-[2fr_1fr]">

<>![Nav](/docs/nav-layout-home.png)</>

<>![Nav](/docs/nav-layout-docs.png)</>

</div>

```tsx tab="Shared Options" title="app/layout.config.tsx"
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export const baseOptions: BaseLayoutProps = {
  links: [], // [!code highlight]
  // other options
};
```

```tsx tab="Docs Layout" title="app/docs/layout.tsx"
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import { baseOptions } from '@/app/layout.config';
import { source } from '@/lib/source';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout
      {...baseOptions}
      tree={source.pageTree}
      links={[]} // [!code highlight]
    >
      {children}
    </DocsLayout>
  );
}
```

```tsx tab="Home Layout" title="app/(home)/layout.tsx"
import { HomeLayout } from 'fumadocs-ui/layouts/home';
import { baseOptions } from '@/app/layout.config';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <HomeLayout
      {...baseOptions}
      links={[]} // [!code highlight]
    >
      {children}
    </HomeLayout>
  );
}
```

You can see all supported items below:

### Link Item

A link to navigate to a URL/href, can be external.

```tsx title="app/layout.config.tsx"
import { BookIcon } from 'lucide-react';
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export const baseOptions: BaseLayoutProps = {
  links: [
    {
      icon: <BookIcon />,
      text: 'Blog',
      url: '/blog',
      // secondary items will be displayed differently on navbar
      secondary: false,
    },
  ],
};
```

#### Active Mode

The conditions to be marked as active.

| Mode         | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| `url`        | When browsing the specified url                             |
| `nested-url` | When browsing the url and its child pages like `/blog/post` |
| `none`       | Never be active                                             |

```tsx title="app/layout.config.tsx"
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export const baseOptions: BaseLayoutProps = {
  links: [
    {
      text: 'Blog',
      url: '/blog',
      active: 'nested-url',
    },
  ],
};
```

### Icon Item

Same as link item, but is shown as an icon button.
Icon items are secondary by default.

```tsx title="app/layout.config.tsx"
import { BookIcon } from 'lucide-react';
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export const baseOptions: BaseLayoutProps = {
  links: [
    {
      type: 'icon',
      label: 'Visit Blog', // `aria-label`
      icon: <BookIcon />,
      text: 'Blog',
      url: '/blog',
    },
  ],
};
```

### Custom Item

Display a custom component.

```tsx title="app/layout.config.tsx"
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export const baseOptions: BaseLayoutProps = {
  links: [
    {
      type: 'custom',
      children: <Button variant="primary">Login</Button>,
      secondary: true,
    },
  ],
};
```

### GitHub URL

There's also a shortcut for adding GitHub repository link item.

```tsx twoslash title="app/layout.config.tsx"
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export const baseOptions: BaseLayoutProps = {
  githubUrl: 'https://github.com',
};
```

### Normal Menu

A menu containing multiple link items.

```tsx title="app/layout.config.tsx"
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export const baseOptions: BaseLayoutProps = {
  links: [
    {
      type: 'menu',
      text: 'Guide',
      items: [
        {
          text: 'Getting Started',
          description: 'Learn to use Fumadocs',
          url: '/docs',
        },
      ],
    },
  ],
};
```

### Navigation Menu

In Home Layout, you can add navigation menu (fully animated) to the navbar.

![Nav](/docs/nav-layout-menu.png)

```tsx title="app/(home)/layout.tsx"
import { baseOptions } from '@/app/layout.config';
import type { ReactNode } from 'react';
import { HomeLayout } from 'fumadocs-ui/layouts/home';
import {
  NavbarMenu,
  NavbarMenuContent,
  NavbarMenuLink,
  NavbarMenuTrigger,
} from 'fumadocs-ui/layouts/home/navbar';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <HomeLayout
      {...baseOptions}
      links={[
        {
          type: 'custom',
          // only displayed on navbar, not mobile menu
          on: 'nav',
          children: (
            <NavbarMenu>
              <NavbarMenuTrigger>Documentation</NavbarMenuTrigger>
              <NavbarMenuContent>
                <NavbarMenuLink href="/docs">Hello World</NavbarMenuLink>
              </NavbarMenuContent>
            </NavbarMenu>
          ),
        },
        // other items
      ]}
    >
      {children}
    </HomeLayout>
  );
}
```
`````

## File: apps/docs/content/docs/ui/navigation/sidebar.mdx
`````
---
title: Sidebar Links
description: Customise sidebar navigation links on Docs Layout.
---

## Overview

<div className='flex justify-center items-center *:max-w-[200px] bg-gradient-to-br from-fd-primary/10 rounded-xl border'>

    ![Sidebar](/docs/sidebar.png)

</div>

Sidebar items are rendered from the page tree you passed to `<DocsLayout />`.

For `source.pageTree`, it generates the tree from your file structure, you can see [Routing](/docs/ui/page-conventions) for available patterns.

```tsx title="layout.tsx"
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import { source } from '@/lib/source';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout
      tree={source.pageTree}
      // other props
    >
      {children}
    </DocsLayout>
  );
}
```

You may hardcode it too:

```tsx title="layout.tsx"
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout
      tree={{
        name: 'docs',
        children: [],
      }}
      // other props
    >
      {children}
    </DocsLayout>
  );
}
```

### Sidebar Tabs (Dropdown)

Sidebar Tabs are folders with tab-like behaviours, only the content of opened tab will be visible.

<div className='flex justify-center items-center *:max-w-[360px] bg-gradient-to-br from-fd-primary/10 rounded-xl border'>

    ![Sidebar Tabs](/docs/sidebar-tabs.png)

</div>

By default, the tab trigger will be displayed as a **Dropdown** component (hidden unless one of its items is active).

You can add items by marking folders as [Root Folders](/docs/ui/page-conventions#root-folder), create a `meta.json` file in the folder:

```json title="content/docs/my-folder/meta.json"
{
  "title": "Name of Folder",
  "description": "The description of root folder (optional)",
  "root": true
}
```

Or specify them explicitly:

```tsx title="/app/docs/layout.tsx"
import { DocsLayout } from 'fumadocs-ui/layouts/docs';

<DocsLayout
  sidebar={{
    tabs: [
      {
        title: 'Components',
        description: 'Hello World!',
        // active for `/docs/components` and sub routes like `/docs/components/button`
        url: '/docs/components',

        // optionally, you can specify a set of urls which activates the item
        // urls: new Set(['/docs/test', '/docs/components']),
      },
    ],
  }}
/>;
```

Set it to `false` to disable:

```tsx
import { DocsLayout } from 'fumadocs-ui/layouts/docs';

<DocsLayout sidebar={{ tabs: false }} />;
```

<Callout title="Want further customisations?">

You can specify a `banner` to the [Docs Layout](/docs/ui/layouts/docs) component.

```tsx
import { DocsLayout, type DocsLayoutProps } from 'fumadocs-ui/layouts/docs';
import type { ReactNode } from 'react';
import { baseOptions } from '@/app/layout.config';
import { source } from '@/lib/source';

const docsOptions: DocsLayoutProps = {
  ...baseOptions,
  tree: source.pageTree,
  sidebar: {
    banner: <div>Hello World</div>,
  },
};

export default function Layout({ children }: { children: ReactNode }) {
  return <DocsLayout {...docsOptions}>{children}</DocsLayout>;
}
```

</Callout>

#### Decoration

Change the icon/styles of tabs.

```tsx
import { DocsLayout } from 'fumadocs-ui/layouts/docs';

<DocsLayout
  sidebar={{
    tabs: {
      transform: (option, node) => ({
        ...option,
        icon: <MyIcon />,
      }),
    },
  }}
/>;
```
`````

## File: apps/docs/content/docs/ui/search/.shared.mdx
`````
### Replace Search Dialog

To use your own search dialog, make a client-side `<RootProvider />` wrapper, and replace the original root provider with it.

```tsx tab="provider.tsx"
'use client';
import { RootProvider } from 'fumadocs-ui/provider';
// your custom dialog [!code highlight]
import SearchDialog from '@/components/search';
import type { ReactNode } from 'react';

export function Provider({ children }: { children: ReactNode }) {
  return (
    <RootProvider
      search={{
        SearchDialog,
      }}
    >
      {children}
    </RootProvider>
  );
}
```

```tsx tab="app/layout.tsx"
import { Provider } from './provider';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        {/* [!code ++] */}
        <Provider>{children}</Provider>
      </body>
    </html>
  );
}
```
`````

## File: apps/docs/content/docs/ui/search/.tag-filter.mdx
`````
```tsx
'use client';

import {
  SearchDialog,
  SearchDialogContent,
  SearchDialogFooter,
  SearchDialogOverlay,
  type SharedProps,
  TagsList,
  TagsListItem,
} from 'fumadocs-ui/components/dialog/search';
import { useState } from 'react';
import { useDocsSearch } from 'fumadocs-core/search/client';

export default function CustomSearchDialog(props: SharedProps) {
  // [!code ++]
  const [tag, setTag] = useState<string | undefined>();
  const { search, setSearch, query } = useDocsSearch({
    tag, // [!code ++]
    // other options depending on your search engine
  });

  return (
    <SearchDialog>
      <SearchDialogOverlay />
      <SearchDialogContent>
        ...
        <SearchDialogFooter className="flex flex-row">
          {/* [!code ++:3] */}
          <TagsList tag={tag} onTagChange={setTag}>
            <TagsListItem value="my-value">My Value</TagsListItem>
          </TagsList>
        </SearchDialogFooter>
      </SearchDialogContent>
    </SearchDialog>
  );
}
```
`````

## File: apps/docs/content/docs/ui/search/algolia.mdx
`````
---
title: Algolia
description: Using Algolia with Fumadocs UI.
---

## Overview

For the setup guide, see [Integrate Algolia Search](/docs/headless/search/algolia).

While generally we recommend building your own search with their client-side
SDK, you can also plug the built-in dialog interface.

## Setup

Create a search dialog, replace `appId`, `apiKey` and `indexName` with your desired values.

<include meta='title="components/search.tsx"'>./algolia.tsx</include>

<Callout title="Note" className='mt-4'>

    `useDocsSearch()` doesn't use instant search (their official
    Javascript client).

</Callout>

<include>.shared.mdx</include>

### Tag Filter

Optionally, you can add UI for filtering results by tags. Configure [Tag Filter](/docs/headless/search/algolia#tag-filter) on search server and add the following:

<include>.tag-filter.mdx</include>
`````

## File: apps/docs/content/docs/ui/search/index.mdx
`````
---
title: Search
description: Implement document search in your docs
---

## Search UI

You can customise some configurations from root provider.

For example, to disable search UI:

```tsx title="app/layout.tsx"
import { RootProvider } from 'fumadocs-ui/provider';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <html>
      <body>
        <RootProvider
          search={{
            enabled: false, // [!code ++]
          }}
        >
          {children}
        </RootProvider>
      </body>
    </html>
  );
}
```

For further customisations, you can see [Search Client](#search-client).

### Hot Keys

Customise the hot keys to trigger search dialog, by default it's <kbd>⌘</kbd> <kbd>K</kbd> or <kbd>Ctrl</kbd> <kbd>K</kbd>.

```tsx
import { RootProvider } from 'fumadocs-ui/provider';

<RootProvider
  search={{
    hotKey: [
      {
        display: 'K',
        key: 'k', // key code, or a function determining whether the key is pressed
      },
    ],
  }}
>
  {children}
</RootProvider>;
```

## Search Client

You can choose & configure the search client according to your search engine, it defaults to Orama search.

<DocsCategory />

### Community Integrations

A list of integrations maintained by community.

- [Trieve Search](/docs/headless/search/trieve)
`````

## File: apps/docs/content/docs/ui/search/mixedbread.mdx
`````
---
title: Mixedbread
description: Using Mixedbread with Fumadocs UI.
---

## Overview

For the setup guide, see [Integrate Mixedbread Search](/docs/headless/search/mixedbread).

## Setup

Create a search dialog, replace `apiKey` and `vectorStoreId` with your desired values.

<include meta='title="components/search.tsx"'>./mixedbread.tsx</include>

<include>.shared.mdx</include>

### Tag Filter

Optionally, you can add UI for filtering results by tags. Configure [Tag Filter](/docs/headless/search/mixedbread#tag-filter) on search server and add the following:

<include>.tag-filter.mdx</include>
`````

## File: apps/docs/content/docs/ui/search/orama-cloud.mdx
`````
---
title: Orama Cloud
description: Using Orama Cloud with Fumadocs UI.
---

## Setup

For the setup guide, see [Integrate Orama Cloud](/docs/headless/search/orama-cloud).

Create a search dialog, replace `endpoint` and `api_key` with your desired values.

<include meta='title="components/search.tsx"'>orama-cloud.tsx</include>

<include>.shared.mdx</include>
`````

## File: apps/docs/content/docs/ui/search/orama.mdx
`````
---
title: Orama (default)
description: The default search engine powered by Orama.
---

## Overview

Fumadocs configures [Orama search engine](/docs/headless/search/orama) out-of-the-box.

It works through a API endpoint (route handler), or a statically cached file for Next.js apps using Static Export.

## Setup

Create a search dialog.

<Tabs items={['fetch (default)', 'static']}>

    <Tab>

The UI has been configured by default, you can also re-create it for further customisations:

<include meta='title="components/search.tsx"'>fetch.tsx</include>

    </Tab>

    <Tab id='static'>

For Static Export, you can configure [static mode](/docs/headless/search/orama#static-export) on search server, and use the `static` client:

```package-install
@orama/orama
```

<include meta='title="components/search.tsx"'>./static.tsx</include>

    </Tab>

</Tabs>

<include>.shared.mdx</include>

### Tag Filter

Optionally, you can add UI for filtering results by tags. Configure [Tag Filter](/docs/headless/search/orama#tag-filter) on search server and add the following:

<include>.tag-filter.mdx</include>
`````

## File: apps/docs/content/docs/ui/comparisons.mdx
`````
---
title: Comparisons
description: How is Fumadocs different from other existing frameworks?
icon: GitCompareArrows
---

## Nextra

Fumadocs is highly inspired by Nextra. For example, the Routing Conventions. That is why
`meta.json` also exists in Fumadocs.

Nextra is more opinionated than Fumadocs. Fumadocs is accelerated by App Router. As a result, It provides many server-side functions, and you have to
configure things manually compared to simply editing a configuration file.

Fumadocs works great if you want more control over everything, such as
adding it to an existing codebase or implementing advanced routing.

### Feature Table

| Feature             | Fumadocs     | Nextra                    |
| ------------------- | ------------ | ------------------------- |
| Static Generation   | Yes          | Yes                       |
| Cached              | Yes          | Yes                       |
| Light/Dark Mode     | Yes          | Yes                       |
| Syntax Highlighting | Yes          | Yes                       |
| Table of Contents   | Yes          | Yes                       |
| Full-text Search    | Yes          | Yes                       |
| i18n                | Yes          | Yes                       |
| Last Git Edit Time  | Yes          | Yes                       |
| Page Icons          | Yes          | Yes, via `_meta.js` files |
| RSC                 | Yes          | Yes                       |
| Remote Source       | Yes          | Yes                       |
| SEO                 | Via Metadata | Yes                       |
| Built-in Components | Yes          | Yes                       |
| RTL Layout          | Yes          | Yes                       |

### Additional Features

Features supported via 3rd party libraries like [TypeDoc](https://typedoc.org) will not be listed here.

| Feature                    | Fumadocs | Nextra |
| -------------------------- | -------- | ------ |
| OpenAPI Integration        | Yes      | No     |
| TypeScript Docs Generation | Yes      | No     |
| TypeScript Twoslash        | Yes      | Yes    |

## Mintlify

Mintlify is a documentation service, as compared to Fumadocs, it offers a free tier but isn't completely free and open source.

Fumadocs is not as powerful as Mintlify, for example, the OpenAPI integration of Mintlify.
As the creator of Fumadocs, I wouldn't recommend switching to Fumadocs from Mintlify if you're satisfied with the current way you build docs.
However, I believe Fumadocs is a suitable tool for all Next.js developers who want to have elegant docs.

## Docusaurus

Docusaurus is a powerful framework based on React.js. It offers many cool
features with plugins and custom themes.

### Better DX

Since Fumadocs is built on the top of Next.js, you'll have to start the Next.js dev
server every time to review changes, and initial boilerplate code is relatively more
compared to Docusaurus.

For a simple docs, Docusaurus might be a better choice if you don't need any Next.js specific functionality.

However, when you want to use Next.js, or seek extra customizability like tuning default UI components, Fumadocs could be a better choice.

### Plugins

You can easily achieve many things with plugins, their ecosystem is indeed larger and maintained by many contributors.

In comparison, the flexibility of Fumadocs allows you to implement them on your own, it may take longer to tune it to your satisfaction.
`````

## File: apps/docs/content/docs/ui/customisation.mdx
`````
---
title: Overview
description: An overview of Fumadocs UI
---

## Architecture

<UiOverview />

|               |                                                         |
| ------------- | ------------------------------------------------------- |
| **Sidebar**   | Display site title and navigation elements.             |
| **Page Tree** | Passed by you, mainly rendered as the items of sidebar. |
| **Docs Page** | All content of the page.                                |
| **TOC**       | Navigation within the article.                          |

## Customisation

### Layouts

You can use the exposed options of different layouts:

<Cards>
  <Card title="Docs Layout" href="/docs/ui/layouts/docs">
    Layout for docs
  </Card>
  <Card title="Docs Page" href="/docs/ui/layouts/page">
    Layout for docs content
  </Card>
  <Card title="Notebook Layout" href="/docs/ui/layouts/notebook">
    A more compact version of Docs Layout
  </Card>
  <Card title="Home Layout" href="/docs/ui/layouts/home-layout">
    Layout for other pages
  </Card>
</Cards>

### Components

Fumadocs UI also offers styled components for interactive examples to enhance your docs, you can customise them with exposed props like `style` and `className`.

See [Components](/docs/ui/components).

### Design System

Since the design system is built on Tailwind CSS, you can customise it [with CSS Variables](/docs/ui/theme#colors).

### CLI

Fumadocs CLI is a tool that installs components to your codebase, similar to Shadcn UI.

```package-install
npx @fumadocs/cli
```

Use it to install Fumadocs UI components:

```package-install
npx @fumadocs/cli add
```

Or customise layouts:

```package-install
npx @fumadocs/cli customise
```
`````

## File: apps/docs/content/docs/ui/index.mdx
`````
---
title: Quick Start
description: Getting Started with Fumadocs
icon: Album
---

## Introduction

Fumadocs <span className='text-fd-muted-foreground text-sm'>(Foo-ma docs)</span> is a **documentation framework** based on Next.js, designed to be fast, flexible,
and composes seamlessly into Next.js App Router.

Fumadocs has different parts:

<Cards>

<Card icon={<CpuIcon className="text-purple-300" />} title='Fumadocs Core'>

Handles most of the logic, including document search, content source adapters, and Markdown extensions.

</Card>

<Card icon={<PanelsTopLeft className="text-blue-300" />} title='Fumadocs UI'>

The default theme of Fumadocs offers a beautiful look for documentation sites and interactive components.

</Card>

<Card icon={<Database />} title='Content Source'>

The source of your content, can be a CMS or local data layers like [Fumadocs MDX](/docs/mdx) (the official content source).

</Card>

<Card icon={<Terminal />} title='Fumadocs CLI'>

A command line tool to install UI components and automate things, useful for customizing layouts.

</Card>

</Cards>

<Callout title="Want to learn more?">
  Read our in-depth [What is Fumadocs](/docs/ui/what-is-fumadocs) introduction.
</Callout>

### Terminology

**Markdown/MDX:** Markdown is a markup language for creating formatted text. Fumadocs supports Markdown and MDX (superset of Markdown) out-of-the-box.

Although not required, some basic knowledge of Next.js App Router would be useful for further customisations.

## Automatic Installation

A minimum version of Node.js 18 required, note that Node.js 23.1 might have problems with Next.js production build.

```bash tab="npm"
npm create fumadocs-app
```

```bash tab="pnpm"
pnpm create fumadocs-app
```

```bash tab="yarn"
yarn create fumadocs-app
```

```bash tab="bun"
bun create fumadocs-app
```

It will ask you:

- the React.js framework to use (the docs is only written for Next.js).
- the content source to use.

A new fumadocs app should be initialized. Now you can start hacking!

<Callout title='From Existing Codebase?'>

    You can follow the [Manual Installation](/docs/ui/manual-installation) guide to get started.

</Callout>

### Enjoy!

Create your first MDX file in the docs folder.

```mdx title="content/docs/index.mdx"
---
title: Hello World
---

## Yo what's up
```

Run the app in development mode and see http://localhost:3000/docs.

```npm
npm run dev
```

## FAQ

Some common questions you may encounter.

<Accordions>
    <Accordion id='change-base-url' title="How to change the base route of docs?">

Since Fumadocs uses Next.js App Router, you can change the base route of docs (e.g. from `/docs/page` to `/info/page`) by renaming the route:

<Files>
  <Folder name="app/docs" defaultOpen className="opacity-50" disabled>
    <File name="layout.tsx" />
  </Folder>
  <Folder name="app/info" defaultOpen>
    <File name="layout.tsx" />
  </Folder>
</Files>

And update the base URL of pages in `source.ts`:

```ts title="lib/source.ts"
import { loader } from 'fumadocs-core/source';

export const source = loader({
  baseUrl: '/info', // [!code highlight]
});
```

If you want to remove the entire base route (docs start at `/` instead of `/docs`), it's the same logic.

Make your docs folder a route group.

<Files>
  <Folder name="app/(docs)" defaultOpen>
    <File name="layout.tsx" />
  </Folder>
</Files>

And update `baseUrl`:

```ts title="lib/source.ts"
import { loader } from 'fumadocs-core/source';

export const source = loader({
  baseUrl: '/', // [!code highlight]
});
```

    </Accordion>
    <Accordion id='dynamic-route' title="It uses Dynamic Route, will it be poor in performance?">

Next.js turns dynamic route into static routes when `generateStaticParams` is configured.
Hence, it is as fast as static pages.

You can enable Static Exports on Next.js to get a static build output. (Notice that Route Handler doesn't work with static export, you have to configure static search)

    </Accordion>
    <Accordion id='custom-layout-docs-page' title='How to create a page in /docs without docs layout?'>

Same as managing layouts in Next.js App Router, remove the original MDX file from content directory (`/content/docs`).
This ensures duplicated pages will not cause errors.

Now, You can add the page to another route group, which isn't a descendant of docs layout.

For example, to replace `/docs/test`:

<Files>
  <File name="(home)/docs/test/page.tsx" />
  <Folder name="docs">
    <File name="layout.tsx" />
    <File name="[[...slug]]/page.tsx" />
  </Folder>
</Files>

For `/docs`, you need to change the catch-all route to be non-optional:

<Files>
  <File name="(home)/docs/page.tsx" />
  <Folder name="docs" defaultOpen>
    <File name="layout.tsx" />
    <File name="[...slug]/page.tsx" />
  </Folder>
</Files>

    </Accordion>

    <Accordion id='multi-docs' title="How to implement multi-docs?">
        We recommend to use [Sidebar Tabs](/docs/ui/navigation/sidebar#sidebar-tabs).
    </Accordion>

</Accordions>

### Upgrade Fumadocs

Make sure to upgrade Fumadocs when you've encountered any problems or trying out new features:

```bash title="pnpm"
pnpm update -i -r --latest
```

## Learn More

New to here? Don't worry, we are welcome for your questions.

If you find anything confusing, please give your feedback on [Github Discussion](https://github.com/fuma-nama/fumadocs/discussions)!

### Writing Content

For authoring docs, make sure to read:

<Cards>
  <Card href="/docs/ui/markdown" title="Markdown">
    Fumadocs has some additional features for authoring content.
  </Card>
  <Card href="/docs/ui/navigation" title="Navigation">
    Learn how to customise navigation links and sidebar items.
  </Card>
  <Card href="/docs/ui/page-conventions" title="Routing">
    Learn how to organise content.
  </Card>
  <Card
    href="/docs/ui/components"
    title="Components"
    description="See all available components to enhance your docs"
  />
</Cards>

### Special Needs

<Cards>
  <Card
    href="/docs/ui/static-export"
    title="Configure Static Export"
    description="Learn how to enable static export on your docs"
  />
  <Card
    href="/docs/ui/internationalization"
    title="Internationalization"
    description="Learn how to enable i18n"
  />
  <Card
    href="/docs/ui/theme"
    title="Color Themes"
    description="Add themes to Fumadocs UI"
  />
  <Card
    href="/docs/ui/customisation"
    title="Customise UI"
    description="A detailed guide on how to customise UI"
  />
</Cards>
`````

## File: apps/docs/content/docs/ui/internationalization.mdx
`````
---
title: Internationalization
description: Support multiple languages in your documentation
---

## Overview

For Next.js apps, you'll have to configure i18n routing on both Next.js and Fumadocs.

Fumadocs is not a full-powered i18n library, it's up to you when internationalizing the rest of your app.
You can also use other libraries with Fumadocs like [next-intl](https://github.com/amannn/next-intl).

<Callout title="New to Next.js?">
  You can [learn more about i18n in
  Next.js](https://nextjs.org/docs/app/building-your-application/routing/internationalization).
</Callout>

## Setup

Define the i18n configurations in a file, we will import it with `@/lib/i18n` in this guide.

<include cwd meta='title="lib/i18n.ts"'>
  ../../examples/i18n/lib/i18n.ts
</include>

> See [available options](/docs/headless/internationalization) for i18n config.

Pass it to the source loader.

```ts title="lib/source.ts"
import { i18n } from '@/lib/i18n';
import { loader } from 'fumadocs-core/source';

export const source = loader({
  i18n, // [!code ++]
  // other options
});
```

### Middleware

Create a middleware that redirects users to appropriate locale.

<include cwd meta='title="middleware.ts"'>
  ../../examples/i18n/middleware.ts
</include>

<Callout title="Using your own middleware?">

    The default middleware is optional, you can also use your own middleware or the one provided by i18n libraries.

    Make sure its behaviour aligns with the [`hidePrefix`](/docs/headless/internationalization#hide-locale-prefix) option you set in your i18n config.

</Callout>

### Routing

Create a `/app/[lang]` folder, and move your pages/layouts into it, except route handlers.

<Files>
  <Folder name="app" defaultOpen>
    <File name="api/search/route.ts" />
    <Folder name="[lang]" defaultOpen>
      <File name="layout.tsx" />
      <File name="(home)/page.tsx" />
      <File name="..." />
    </Folder>
    <File name="layout.config.tsx" />
  </Folder>
</Files>

<Callout title="Common Mistake" type="error">
  Did you accidentally find your styles lost? Make sure the import path to
  `global.css` is still correct!
</Callout>

Provide UI translations and other config to `<RootProvider />`, the English translations are used when `translations` is not specified.

```tsx title="app/[lang]/layout.tsx"
import { RootProvider } from 'fumadocs-ui/provider';
import type { Translations } from 'fumadocs-ui/i18n';

// [!code ++:17]
// translations
const cn: Partial<Translations> = {
  search: 'Translated Content',
};

// available languages that will be displayed on UI
// make sure `locale` is consistent with your i18n config
const locales = [
  {
    name: 'English',
    locale: 'en',
  },
  {
    name: 'Chinese',
    locale: 'cn',
  },
];

export default async function RootLayout({
  params,
  children,
}: {
  params: Promise<{ lang: string }>;
  children: React.ReactNode;
}) {
  const lang = (await params).lang;

  return (
    <html lang={lang}>
      <body>
        <RootProvider
          i18n={{
            locale: lang, // [!code ++]
            locales, // [!code ++]
            translations: { cn }[lang], // [!code ++]
          }}
        >
          {children}
        </RootProvider>
      </body>
    </html>
  );
}
```

### Pass Locale

Pass the locale to Fumadocs in your pages and layouts.

```tsx title="app/layout.config.tsx" tab="Shared Options"
import { i18n } from '@/lib/i18n';
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

// Make `baseOptions` a function: [!code highlight]
export function baseOptions(locale: string): BaseLayoutProps {
  return {
    i18n, // [!code ++]
    // different props based on `locale`
  };
}
```

```tsx title="/app/[lang]/(home)/layout.tsx" tab="Home Layout"
import type { ReactNode } from 'react';
import { HomeLayout } from 'fumadocs-ui/layouts/home';
import { baseOptions } from '@/app/layout.config';

export default async function Layout({
  params,
  children,
}: {
  params: Promise<{ lang: string }>;
  children: ReactNode;
}) {
  const { lang } = await params;

  return <HomeLayout {...baseOptions(lang)}>{children}</HomeLayout>; // [!code highlight]
}
```

```tsx title="/app/[lang]/docs/layout.tsx" tab="Docs Layout"
import type { ReactNode } from 'react';
import { source } from '@/lib/source';
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import { baseOptions } from '@/app/layout.config';

export default async function Layout({
  params,
  children,
}: {
  params: Promise<{ lang: string }>;
  children: ReactNode;
}) {
  const { lang } = await params;

  return (
    // [!code highlight]
    <DocsLayout {...baseOptions(lang)} tree={source.pageTree[lang]}>
      {children}
    </DocsLayout>
  );
}
```

```ts title="page.tsx" tab="Docs Page"
import { source } from '@/lib/source';

export default async function Page({
  params,
}: {
  params: Promise<{ lang: string; slug?: string[] }>;
}) {
  const { slug, lang } = await params;
  // get page
  source.getPage(slug); // [!code --]
  source.getPage(slug, lang); // [!code ++]

  // get pages
  source.getPages(); // [!code --]
  source.getPages(lang); // [!code ++]
}
```

<Callout title={<>Using another name for <code>lang</code> dynamic segment?</>}>

If you're using another name like `app/[locale]`, you also need to update `generateStaticParams()` in docs page:

```tsx
export function generateStaticParams() {
  return source.generateParams(); // [!code --]
  return source.generateParams('slug', 'locale'); // [!code ++] new param name
}
```

</Callout>

### Search

Configure i18n on your search solution.

- **Built-in Search (Orama):** See [Internationalization](/docs/headless/search/orama#internationalization).
- **Cloud Solutions (e.g. Algolia):** They usually have official support for multilingual.

## Writing Documents

<include>../../shared/page-conventions.i18n.mdx</include>

## Navigation

Fumadocs only handles navigation for its own layouts (e.g. sidebar).
For other places, you can use the `useParams` hook to get the locale from url, and attend it to `href`.

```tsx
import Link from 'next/link';
import { useParams } from 'next/navigation';

const { lang } = useParams();

return <Link href={`/${lang}/another-page`}>This is a link</Link>;
```

In addition, the [`fumadocs-core/dynamic-link`](/docs/headless/components/link#dynamic-hrefs) component supports dynamic hrefs, you can use it to attend the locale prefix.
It is useful for Markdown/MDX content.

```mdx title="content.mdx"
import { DynamicLink } from 'fumadocs-core/dynamic-link';

<DynamicLink href="/[lang]/another-page">This is a link</DynamicLink>
```
`````

## File: apps/docs/content/docs/ui/manual-installation.mdx
`````
---
title: Manual Installation
description: Add Fumadocs to existing projects.
---

Before continuing, make sure:

- Next.js 15 and Tailwind CSS 4 are configured.

## Getting Started

```npm
npm i fumadocs-ui fumadocs-core
```

### Content Source

Fumadocs supports different content sources, including Fumadocs MDX and [Content Collections](/docs/headless/content-collections).

Fumadocs MDX is our official content source, you can configure it with:

```package-install
fumadocs-mdx @types/mdx
```

```js tab="next.config.mjs"
import { createMDX } from 'fumadocs-mdx/next';

const withMDX = createMDX();

/** @type {import('next').NextConfig} */
const config = {
  reactStrictMode: true,
};

export default withMDX(config);
```

<include cwd meta='tab="mdx-components.tsx"'>
  ../../examples/next-mdx/mdx-components.tsx
</include>

```ts tab="source.config.ts"
import { defineDocs } from 'fumadocs-mdx/config';

export const docs = defineDocs({
  dir: 'content/docs',
});
```

```json tab="package.json"
{
  "scripts": {
    "postinstall": "fumadocs-mdx" // [!code ++]
  }
}
```

Finally, to access your content:

```ts title="lib/source.ts"
// .source folder will be generated when you run `next dev`
import { docs } from '@/.source';
import { loader } from 'fumadocs-core/source';

export const source = loader({
  baseUrl: '/docs',
  source: docs.toFumadocsSource(),
});
```

### Root Layout

Wrap the entire application inside [Root Provider](/docs/ui/layouts/root-provider), and add required styles to `body`.

```tsx title="app/layout.tsx"
import { RootProvider } from 'fumadocs-ui/provider';
import type { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        // you can use Tailwind CSS too
        style={{
          display: 'flex',
          flexDirection: 'column',
          minHeight: '100vh',
        }}
      >
        <RootProvider>{children}</RootProvider>
      </body>
    </html>
  );
}
```

### Styles

Add the following Tailwind CSS styles to `global.css`.

```css title="global.css"
@import 'tailwindcss';
@import 'fumadocs-ui/css/neutral.css';
@import 'fumadocs-ui/css/preset.css';
```

> It doesn't come with a default font, you may choose one from `next/font`.

### Layout

Create a `app/layout.config.tsx` file to put the shared options for our layouts.

<include cwd meta='title="app/layout.config.tsx"'>
  ../../examples/next-mdx/app/layout.config.tsx
</include>

Create a folder `/app/docs` for our docs, and give it a proper layout.

<include cwd meta='title="app/docs/layout.tsx"'>
  ../../examples/next-mdx/app/docs/layout.tsx
</include>

> `pageTree` refers to Page Tree, it should be provided by your content source.

### Page

Create a catch-all route `/app/docs/[[...slug]]` for docs pages.

In the page, wrap your content in the [Page](/docs/ui/layouts/page) component.

<CodeBlockTabs groupId='content-source'>

    <include cwd meta='title="app/docs/[[...slug]]/page.tsx" tab="Fumadocs MDX"'>../../examples/next-mdx/app/docs/[[...slug]]/page.tsx</include>

    <include cwd meta='title="app/docs/[[...slug]]/page.tsx" tab="Content Collections"'>../../examples/content-collections/app/docs/[[...slug]]/page.tsx</include>

</CodeBlockTabs>

### Search

Use the default document search based on Orama.

<include cwd meta='title="app/api/search/route.ts"'>
  ../../examples/next-mdx/app/api/search/route.ts
</include>

Learn more about [Document Search](/docs/headless/search).

### Done

You can start the dev server and create MDX files.

```mdx title="content/docs/index.mdx"
---
title: Hello World
---

## Introduction

I love Anime.
```

## Deploying

It should work out-of-the-box with Vercel & Netlify.

### Cloudflare

Use https://opennext.js.org/cloudflare, Fumadocs doesn't work on Edge runtime.

### Docker Deployment

If you want to deploy your Fumadocs app using Docker with **Fumadocs MDX configured**, make sure to add the `source.config.ts` file to the `WORKDIR` in the Dockerfile.
The following snippet is taken from the official [Next.js Dockerfile Example](https://github.com/vercel/next.js/blob/canary/examples/with-docker/Dockerfile):

```zsh title="Dockerfile"
# syntax=docker.io/docker/dockerfile:1

FROM node:18-alpine AS base

# Install dependencies only when needed
FROM base AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
RUN apk add --no-cache libc6-compat
WORKDIR /app

# Install dependencies based on the preferred package manager [!code highlight]
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* .npmrc* source.config.ts ./
RUN \
  if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
  elif [ -f package-lock.json ]; then npm ci; \
  elif [ -f pnpm-lock.yaml ]; then corepack enable pnpm && pnpm i --frozen-lockfile; \
  else echo "Lockfile not found." && exit 1; \
  fi


# Rebuild the source code only when needed
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Next.js collects completely anonymous telemetry data about general usage.
# Learn more here: https://nextjs.org/telemetry
# Uncomment the following line in case you want to disable telemetry during the build.
# ENV NEXT_TELEMETRY_DISABLED=1

RUN \
  if [ -f yarn.lock ]; then yarn run build; \
  elif [ -f package-lock.json ]; then npm run build; \
  elif [ -f pnpm-lock.yaml ]; then corepack enable pnpm && pnpm run build; \
  else echo "Lockfile not found." && exit 1; \
  fi

# Production image, copy all the files and run next
FROM base AS runner
WORKDIR /app

ENV NODE_ENV=production
# Uncomment the following line in case you want to disable telemetry during runtime.
# ENV NEXT_TELEMETRY_DISABLED=1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public

# Automatically leverage output traces to reduce image size
# https://nextjs.org/docs/advanced-features/output-file-tracing
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT=3000

# server.js is created by next build from the standalone output
# https://nextjs.org/docs/pages/api-reference/config/next-config-js/output
ENV HOSTNAME="0.0.0.0"
CMD ["node", "server.js"]
```

This ensures Fumadocs MDX can access your configuration file during builds.
`````

## File: apps/docs/content/docs/ui/page-conventions.mdx
`````
---
title: Routing
description: A shared convention for organizing your documents
---

<include>../headless/page-conventions.mdx</include>
`````

## File: apps/docs/content/docs/ui/static-export.mdx
`````
---
title: Static Export
description: Enable static export with Fumadocs
---

## Overview

Fumadocs is fully compatible with Next.js static export, allowing you to export the app as a static HTML site without a Node.js server.

```js title="next.config.mjs"
/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  output: 'export',

  // Optional: Change links `/me` -> `/me/` and emit `/me.html` -> `/me/index.html`
  // trailingSlash: true,

  // Optional: Prevent automatic `/me` -> `/me/`, instead preserve `href`
  // skipTrailingSlashRedirect: true,
};
```

See [Next.js docs](https://nextjs.org/docs/app/guides/static-exports) for limitations and details.

## Search

### Cloud Solutions

Since the search functionality is powered by remote servers, static export works without configuration.

### Built-in Search

Learn how to [enable static mode](/docs/ui/search/orama#static) on search client.

This enables the route handler to be statically cached into a single file, and search will be computed on browser instead.
`````

## File: apps/docs/content/docs/ui/theme.mdx
`````
---
title: Themes
description: Add Theme to Fumadocs UI
---

## Usage

Only Tailwind CSS v4 is supported, the preset will also include source to Fumadocs UI itself:

```css title="Tailwind CSS"
@import 'tailwindcss';
@import 'fumadocs-ui/css/neutral.css';
@import 'fumadocs-ui/css/preset.css';
```

### Preflight Changes

By using the Tailwind CSS plugin, or the pre-built stylesheet, your default border, text and background
colors will be changed.

### Light/Dark Modes

Fumadocs supports light/dark modes with [`next-themes`](https://github.com/pacocoursey/next-themes), it is included in Root Provider.

See [Root Provider](/docs/ui/layouts/root-provider#theme-provider) to learn more.

### RTL Layout

RTL (Right-to-left) layout is supported.

To enable RTL, set the `dir` prop to `rtl` in body and root provider (required for Radix UI).

```tsx
import { RootProvider } from 'fumadocs-ui/provider';
import type { ReactNode } from 'react';

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body dir="rtl">
        <RootProvider dir="rtl">{children}</RootProvider>
      </body>
    </html>
  );
}
```

### Layout Width

Customise the max width of docs layout with CSS Variables.

```css
:root {
  --fd-layout-width: 1400px;
}
```

<WidthTrigger />

## Tailwind CSS Preset

Fumadocs UI adds its own colors, animations, and utilities with Tailwind CSS preset.

### Colors

It comes with many themes out-of-the-box, you can pick one you prefer.

```css
@import 'fumadocs-ui/css/<theme>.css';
@import 'fumadocs-ui/css/preset.css';
```

<Tabs items={['neutral', 'black', 'vitepress', 'dusk', 'catppuccin', 'ocean', 'purple']}>

    <Tab value='neutral'>

![Neutral](/themes/neutral.png)

    </Tab>

    <Tab value='black'>

![Black](/themes/black.png)

    </Tab>

    <Tab value='vitepress'>

![Vitepress](/themes/vitepress.png)

    </Tab>

    <Tab value='dusk'>

![Dusk](/themes/dusk.png)

    </Tab>

    <Tab value='Catppuccin'>

![Catppuccin](/themes/catppuccin.png)

    </Tab>

    <Tab value='ocean'>

![Ocean](/themes/ocean.png)

    </Tab>

    <Tab value='purple'>

![Purple](/themes/purple.png)

    </Tab>

</Tabs>

The design system was inspired by [Shadcn UI](https://ui.shadcn.com), you can also customize the colors using CSS variables.

```css title="global.css"
:root {
  --color-fd-background: hsl(0, 0%, 100%);
}

.dark {
  --color-fd-background: hsl(0, 0%, 0%);
}
```

For Shadcn UI, you can use the `shadcn` preset instead.
It uses colors from your Shadcn UI theme.

```css
@import 'tailwindcss';
@import 'fumadocs-ui/css/shadcn.css';
@import 'fumadocs-ui/css/preset.css';
```

### Typography

We have a built-in plugin forked from [Tailwind CSS Typography](https://tailwindcss.com/docs/typography-plugin).

The plugin adds a `prose` class and variants to customise it.

```tsx
<div className="prose">
  <h1>Good Heading</h1>
</div>
```

> The plugin works with and only with Fumadocs UI's MDX components, it may conflict with `@tailwindcss/typography`.
> If you need to use `@tailwindcss/typography` over the default plugin, [set a class name option](https://github.com/tailwindlabs/tailwindcss-typography/blob/main/README.md#changing-the-default-class-name) to avoid conflicts.
`````

## File: apps/docs/content/docs/ui/versioning.mdx
`````
---
title: Versioning
description: Implementing multi-version in your docs.
---

## Overview

It's common for developer tool related docs to version their docs, such as different docs for v1 and v2 of the same tool.

Fumadocs provide the primitives for you to implement versioning on your own way.

## Partial Versioning

When versioning only applies to part of your docs, You can separate them by folders.

For example:

<Files>
  <Folder name="java-sdk" defaultOpen>
    <Folder name="v1" defaultOpen>
      <File name="getting-started.mdx" />
    </Folder>
    <Folder name="v2" defaultOpen>
      <File name="getting-started.mdx" />
    </Folder>
  </Folder>
</Files>

<Callout title="Good to Know">
  You may want to group them with tabs rather than folders [using Sidebar
  Tabs](/docs/ui/navigation/sidebar#sidebar-tabs).
</Callout>

## Full Versioning

Sometimes you want to version the entire website, such as https://v14.fumadocs.dev (Fumadocs v14) and https://fumadocs.dev (Latest Fumadocs).

You can create a Git branch for a version of docs (call it `v2` for example), and deploy it as a separate app on another subdomain like `v2.my-site.com`.

Optionally, you can link to the other versions from your docs.
This design allows some advantages over partial versioning:

- Easy maintenance: Old docs/branches won't be affected when you iterate or upgrade dependencies.
- Better consistency: Not just the docs itself, your landing page (and other pages) will also be versioned.
`````

## File: apps/docs/content/docs/ui/what-is-fumadocs.mdx
`````
---
title: What is Fumadocs
description: Introducing Fumadocs, a docs framework that you can break.
icon: CircleQuestionMark
---

Fumadocs was created because I wanted a more customisable experience for building docs, to be a docs framework that is not opinionated, **a "framework" that you can break**.

## Philosophy

**Less Abstraction:** Fumadocs expects you to write code and cooperate with the rest of your software.
While most frameworks are configured with a configuration file, they usually lack flexibility when you hope to tune its details.
You can’t control how they render the page nor the internal logic. Fumadocs shows you how the app works, instead of a single configuration file.

**Next.js Fundamentals:** It gives you the utilities and a good-looking UI.
You are still using features of Next.js App Router, like **Static Site Generation**. There is nothing new for Next.js developers, so you can use it with confidence.

**Opinionated on UI:** The only thing Fumadocs UI (the default theme) offers is **User Interface**. The UI is opinionated for bringing better mobile responsiveness and user experience.
Instead, we use a much more flexible approach inspired by Shadcn UI — [Fumadocs CLI](/docs/cli), so we can iterate our design quick, and welcome for more feedback about the UI.

## Why Fumadocs

Fumadocs is designed with flexibility in mind.

You can use `fumadocs-core` as a headless UI library and bring your own styles.
Fumadocs MDX is also a useful library to handle MDX content in Next.js. It also includes:

- Many built-in components.
- Typescript Twoslash, OpenAPI, and Math (KaTeX) integrations.
- Fast and optimized by default, natively built on App Router.
- Tight integration with Next.js, you can add it to an existing Next.js project easily.

You can read [Comparisons](/docs/ui/comparisons) if you're interested.

### Documentation

Fumadocs focuses on **authoring experience**, it provides a beautiful theme and many docs automation tools.

It helps you to iterate your codebase faster while never leaving your docs behind.
You can take this site as an example of docs site built with Fumadocs.

### Blog sites

Since Next.js is already a powerful framework, most features can be implemented with **just Next.js**.

Fumadocs provides additional tooling for Next.js, including syntax highlighting, document search, and a default theme (Fumadocs UI).
It helps you to avoid reinventing the wheels.

## When to use Fumadocs

For most of the web applications, vanilla React.js is no longer enough.
Nowadays, we also wish to have a blog, a showcase page, a FAQ page, etc. With a
fancy UI that's breathtaking, in these cases, Fumadocs can help you build the
docs easier, with less boilerplate.

Fumadocs is maintained by Fuma and many contributors, with care on the maintainability of codebase.
While we don't aim to offer every functionality people wanted, we're more focused on making basic features perfect and well-maintained.
You can also help Fumadocs to be more useful by contributing!
`````

## File: apps/docs/content/shared/page-conventions.i18n.mdx
`````
You can add Markdown/meta files for different languages by attending `.{locale}` to your file name, like `page.cn.md` and `meta.cn.json`.

Make sure to create a file for the default locale first, the locale code is optional (e.g. both `get-started.mdx` and `get-started.en.mdx` are accepted).

<Files>
  <Folder name="content/docs" defaultOpen>
    <File name="meta.json" />
    <File name="meta.cn.json" />
    <File name="get-started.mdx" />
    <File name="get-started.cn.mdx" />
  </Folder>
</Files>
`````

## File: apps/docs/public/robots.txt
`````
User-agent: *
Allow: /

Host: https://fumadocs.dev

Sitemap: https://fumadocs.dev/sitemap.xml
`````

## File: examples/content-collections/content/docs/index.mdx
`````
---
title: Hello World
description: Your first document
---

Hey there!

<Callout>Hello World</Callout>

## Heading

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### Heading

#### Heading

| name        | description |
| ----------- | ----------- |
| Hello World | Goodbye     |
`````

## File: examples/content-collections/content/docs/test.mdx
`````
---
title: Hello World
description: Your first document
---

Hey there!

## Heading

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### Heading

```js
console.log('Hello World');
```

#### Heading
`````

## File: examples/i18n/content/docs/index.cn.mdx
`````
---
title: 中文
description: 您的第一個文檔
---

## Hi 中文

Fumadocs 對 i18n 有良好的支持
`````

## File: examples/i18n/content/docs/index.mdx
`````
---
title: Hello World
description: Your first document
---

Hey there!

## Heading

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### Heading

#### Heading
`````

## File: examples/i18n/content/docs/test.mdx
`````
---
title: Hello World
description: Your first document
---

Hey there!

## Heading

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### Heading

```js
console.log('Hello World');
```

#### Heading
`````

## File: examples/next-mdx/content/docs/index.mdx
`````
---
title: Hello World
description: |
  Your first `document`
  ```ts
  console.log("Hello World")
  ```
---

Hey there! fsd asfd sdfsfda
sfd

fdsa ff dsaf sdf sda fasd fsd

## Heading

Hello World dsasfdafsd

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### Heading

#### Heading

| Head                            | Description                         |
| ------------------------------- | ----------------------------------- |
| `hello`                         | Hello World                         |
| very **important**              | Hey                                 |
| _Surprisingly_                  | Fumadocs                            |
| very long text that looks weird | hello world hello world hello world |

<include>./test.mdx</include>
`````

## File: examples/next-mdx/content/docs/test.mdx
`````
---
title: Test
description: A document to test Fumadocs
---

Hey there!

## Cards

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### CodeBlock

```js
console.log('Hello World');
```

#### List

- Hello
- World
`````

## File: examples/next-mdx/content/docs/test2.mdx
`````
---
title: Fumadocs
description: You can just be minimal.
---

## Overview

Fumadocs is a docs framework.
`````

## File: examples/openapi/content/docs/auth.mdx
`````
---
title: 'Authentication'
description: "How to authenticate your requests to Unkey's API"
---

You'll need to authenticate your requests to access some of the endpoints in the Unkey API. In this guide, we'll look at how authentication works.

## Bearer Token

When requesting resources, you will need your root key — you will find it in the [Dashboard](https://app.unkey.com/settings/root-keys). Here's how to add the root key to the request header using cURL:

```bash
curl https://api.unkey.dev/v1/... \
  -H "Authorization: Bearer unkey_xxx"
```

Always keep your root key safe and reset it if you suspect it has been compromised.
`````

## File: examples/openapi/content/docs/index.mdx
`````
---
title: Overview
description: General information about the API.
---

The Unkey API uses HTTP RPC-style methods and generally follow the schema:

```
https://api.unkey.dev/{version}/{service}.{method}
```

For example `GET https://api.unkey.dev/v1/apis.listKeys` to list all keys for an API.

## HTTP Methods

We strictly use only `GET` and `POST` methods. `PUT` and `DELETE` are not used.

### `GET`

`GET` methods are used for reading data. Filtering, sorting, or pagination is done via query parameters.

```http
curl "https://api.unkey.dev/v1/keys.getKey?keyId=key_123" \
  -H "Authorization: Bearer <ROOT_KEY>"
```

### `POST`

`POST` methods are used for creating, updating, and deleting data. Data is passed as `application/json` in the request body.

```http
curl -XPOST "https://api.unkey.dev/v1/keys.createKey" \
  -H "Authorization: Bearer <ROOT_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"apiId": "api_123", "name": "My Key"}'
```
`````

## File: examples/openapi/README.md
`````markdown
# Unkey API Docs

This is an example API documentation based on Unkey's [API documentation](https://github.com/unkeyed/unkey), using Fumadocs OpenAPI.
`````

## File: examples/python/content/docs/index.mdx
`````
---
title: Hello World
description: Your first document
---

Welcome to the docs! You can start writing documents in `/content/docs`.

## What is Next?

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>
`````

## File: examples/python/README.md
`````markdown
1. Use `pnpm python:generate` to generate JSON file locally using Python.
2. Use `pnpm build:docs` to generate docs
`````

## File: examples/react-router/content/docs/index.mdx
`````
---
title: Hello World
description: |
  Your first `document`
  You'll love it!
---

Hey there! Fumadocs is the docs framework that also works on React Router!

## Heading

Hello World

<Cards>
  <Card title="Learn more about React Router" href="https://reactrouter.com" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

```ts
console.log('I love React!');
```

### Heading

#### Heading

| Head                            | Description                         |
| ------------------------------- | ----------------------------------- |
| `hello`                         | Hello World                         |
| very **important**              | Hey                                 |
| _Surprisingly_                  | Fumadocs                            |
| very long text that looks weird | hello world hello world hello world |
`````

## File: examples/react-router/content/docs/test.mdx
`````
---
title: Test
description: A document to test Fumadocs
---

Hey there!

## Cards

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### CodeBlock

```js
console.log('Hello World');
```

#### List

- Hello
- World
`````

## File: examples/react-router/content/docs/test2.mdx
`````
---
title: Fumadocs
description: You can just be minimal.
---

## Overview

Fumadocs is a docs framework.
`````

## File: examples/react-router-i18n/content/docs/index.cn.mdx
`````
---
title: 我喜欢冰淇淋 (Chinese)
---

Hey there! Fumadocs is the docs framework that also works on React Router!

## Heading

Hello World

<Cards>
  <Card title="Learn more about React Router" href="https://reactrouter.com" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

```ts
console.log('I love React!');
```

### Heading

#### Heading

| Head                            | Description                         |
| ------------------------------- | ----------------------------------- |
| `hello`                         | Hello World                         |
| very **important**              | Hey                                 |
| _Surprisingly_                  | Fumadocs                            |
| very long text that looks weird | hello world hello world hello world |
`````

## File: examples/react-router-i18n/content/docs/index.mdx
`````
---
title: Hello World
description: |
  Your first `document`
  You'll love it!
---

Hey there! Fumadocs is the docs framework that also works on React Router!

## Heading

Hello World

<Cards>
  <Card title="Learn more about React Router" href="https://reactrouter.com" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

```ts
console.log('I love React!');
```

### Heading

#### Heading

| Head                            | Description                         |
| ------------------------------- | ----------------------------------- |
| `hello`                         | Hello World                         |
| very **important**              | Hey                                 |
| _Surprisingly_                  | Fumadocs                            |
| very long text that looks weird | hello world hello world hello world |
`````

## File: examples/react-router-i18n/content/docs/test.mdx
`````
---
title: Test
description: A document to test Fumadocs
---

Hey there!

## Cards

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### CodeBlock

```js
console.log('Hello World');
```

#### List

- Hello
- World
`````

## File: examples/remote-mdx/content/docs/comparisons.mdx
`````
---
title: Comparisons
description: How does Fumadocs different from other existing frameworks
---

<Callout type="info">This is for testing Fumadocs MDX Remote</Callout>

## Philosophy

Fumadocs, unlike the other frameworks, it expects you to write code and cooperate with other parts of your software.
While most frameworks are configured with a configuration file, they are usually lack of flexibility when you attempted to complete something more advanced.
You can't control how they render the page, neither the internal logic.

**Fumadocs has no magic:** It gives you the utilities and a good-looking user interface.
You are still using the features of Next.js App Router, configuring Static Site Generation same as a normal Next.js application.
There is nothing new for Next.js developers, you can use it with confidence.

For instance, in this docs, all index pages are rendered dynamically.
Feel free to take a look at the source code of this documentation.

**Opinionated on UI:** The only thing Fumadocs UI offers is **User Interface**, it is opinionated on UI for the best mobile responsibility and user experience.
The design is regularly updated, and we are welcome for feedback about the UI.

## Nextra

Fumadocs is highly inspired by Nextra. For example, the Routing Conventions. That is why
`meta.json` also exists in Fumadocs.

**However, it is not a drop-in replacement for Nextra.**

While we both support a lot of
advanced usages, Nextra is more opinionated than Fumadocs. Fumadocs is accelerated by App Router. As a result, It provides many server-side functions and you have to
configure things manually compared to simply editing a configuration file.

Fumadocs works great if you want more control over everything, such as
adding it to an existing codebase or implementing advanced routing.

### Feature Table

| Feature             | Fumadocs     | Nextra            |
| ------------------- | ------------ | ----------------- |
| Static Generation   | Yes          | Yes               |
| Cached              | Yes          | Yes               |
| Light/Dark Mode     | Yes          | Yes               |
| Syntax Highlighting | Yes          | Yes               |
| Table of Contents   | Yes          | Yes               |
| Full-text Search    | Yes          | Yes               |
| i18n                | Yes          | Yes               |
| Last Git Edit Time  | Yes          | Yes               |
| Page Icons          | Yes          | No                |
| RSC                 | Yes          | Pages Router Only |
| Remote Source       | Yes          | Not Documented    |
| SEO                 | Via Metadata | Yes               |
| Built-in Components | Yes          | Yes               |
| RTL Layout          | Yes          | Yes               |

## Docusaurus

Docusaurus is a powerful framework based on React.js. It offers many cool
features with plugins and custom themes.

### Better DX

Since Fumadocs is built on the top of Next.js, you'll have to start the Next.js dev
server everytime to review changes. And boilerplate code is relatively more
compared to Docusaurus. For a simple docs, Docusaurus might be a better choice
if you don't need any Next.js specific functionality.

### Plugins

You can easily achieve many things with plugins. Although the flexibility of Fumadocs is high, their
eco-system is larger and maintained by many contributors.

### When to use Fumadocs?

For most of the web applications, vanilla React.js is no longer enough.
Nowadays, we also wish to have a blog, a showcase page, a FAQ page, etc. With a
fancy UI that's breathtaking, in these cases, Fumadocs can help you build the
docs easier, with less boilerplate.

## We are working forward

More and more advanced features are rolling out. We currently support
multiple searching solutions including Algolia Search. A good UI and user
experience is always our priority, welcome to give us feedback via Github
discussions!
`````

## File: examples/remote-mdx/content/docs/index.mdx
`````
---
title: Hello World
---

## Testing

```js
console.log('HELLO');
```

Vercel's AI SDK is a powerful tool designed to enhance the development experience by integrating artificial intelligence capabilities into applications. It allows developers to easily implement AI features, such as natural language processing, image recognition, and more, without needing extensive knowledge of machine learning.

Key features of Vercel's AI SDK include:

1. **Seamless Integration**: The SDK can be easily integrated into existing Vercel projects, allowing developers to add AI functionalities with minimal setup.

2. **Pre-built Models**: Vercel provides access to various pre-trained AI models, enabling developers to leverage advanced capabilities without the need for training their own models.

3. **Real-time Processing**: The SDK supports real-time data processing, making it suitable for applications that require immediate responses, such as chatbots or interactive user interfaces.

4. **Scalability**: Built on Vercel's serverless architecture, the AI SDK can scale effortlessly to handle varying loads, ensuring consistent performance.

5. **Documentation and Support**: Vercel offers comprehensive documentation and community support, making it easier for developers to get started and troubleshoot any issues.

Overall, Vercel's AI SDK empowers developers to create innovative applications that harness the power
`````

## File: examples/remote-mdx/content/docs/test.mdx
`````
---
title: Test
---

Hey!

```tsx
'use client';

import { useChat } from 'ai/react';

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit } = useChat({
    maxSteps: 5, // [!code highlight]
  });

  // ... rest of your component code
}
```
`````

## File: examples/tanstack-start/content/index.mdx
`````
---
title: Hello World
description: Your favourite docs framework.
icon: Rocket
---

Hey there! Fumadocs is a docs framework built for Next.js, but do you know it also works on Tanstack Start?

## Heading

Hello World!

<Cards>
  <Card
    title="Learn more about Tanstack Start"
    href="https://tanstack.com/start"
  />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### CodeBlock

```ts
console.log('Hello World');
```

#### Table

| Head                            | Description                         |
| ------------------------------- | ----------------------------------- |
| `hello`                         | Hello World                         |
| very **important**              | Hey                                 |
| _Surprisingly_                  | Fumadocs                            |
| very long text that looks weird | hello world hello world hello world |
`````

## File: examples/tanstack-start/content/test.mdx
`````
---
title: Test
description: This is another page
---

Hello World again!

## Installation

```npm
npm i fumadocs-core fumadocs-ui
```
`````

## File: examples/README.md
`````markdown
## Examples

The apps here are used to generate code examples for our docs.

Please be careful.
`````

## File: packages/cli/CHANGELOG.md
`````markdown
# fumadocs

## 0.2.1

### Patch Changes

- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos

## 0.2.0

### Minor Changes

- ba35933: Support dynamic import transformation

### Patch Changes

- 1d07c67: Replace `execa` with `tinyexec` & removed unused devDeps
- ba35933: Improve dep install UI

## 0.1.1

### Patch Changes

- 482f728: add home layout to customise option

## 0.1.0

### Minor Changes

- 72a3e8c: Add customise command

## 0.0.8

### Patch Changes

- 4be74f6: Improve CLI

## 0.0.7

### Patch Changes

- a16bb23: Improve instructions in i18n plugin

## 0.0.6

### Patch Changes

- 969da26: Improve i18n api

## 0.0.5

### Patch Changes

- c8d9b08: support Next.js 15 i18n auto-config

## 0.0.4

### Patch Changes

- b254ec2: Fix Windows path problems

## 0.0.3

### Patch Changes

- 821e4a0: Fix src folder compatibility of plugins

## 0.0.2

### Patch Changes

- 9d37020: Change name of the package to avoid npm errors

## 0.0.1

### Patch Changes

- 75af7bc: Fix bin directive on index file
`````

## File: packages/content-collections/CHANGELOG.md
`````markdown
# @fumadocs/content-collections

## 1.2.1

### Patch Changes

- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos
- Updated dependencies [7a45921]
- Updated dependencies [1b7bc4b]
  - fumadocs-core@15.5.2

## 1.2.0

### Minor Changes

- 7b4a505: Add `remarkCodeTab` by default

### Patch Changes

- df244e8: Prepare for Content Collections v1
  - fumadocs-core@15.3.4

## 1.1.8

### Patch Changes

- a06af26: Support pages without `title`
- Updated dependencies [08236e1]
- Updated dependencies [a06af26]
  - fumadocs-core@15.0.6

## 1.1.7

### Patch Changes

- a89d6e0: Support Fumadocs v15
- Updated dependencies [5b8cca8]
- Updated dependencies [a763058]
- Updated dependencies [581f4a5]
  - fumadocs-core@15.0.0

## 1.1.6

### Patch Changes

- 3550efc: Fix remark image default config
  - fumadocs-core@14.6.3

## 1.1.5

### Patch Changes

- 8ef00dc: Improve types
- be820c4: Bump deps
- Updated dependencies [e45bc67]
- Updated dependencies [d9e908e]
- Updated dependencies [d9e908e]
- Updated dependencies [f949520]
- Updated dependencies [9a0b09f]
- Updated dependencies [9a0b09f]
- Updated dependencies [367f4c3]
- Updated dependencies [e1ee822]
- Updated dependencies [e612f2a]
- Updated dependencies [9a0b09f]
- Updated dependencies [d9e908e]
- Updated dependencies [8ef00dc]
- Updated dependencies [979e301]
- Updated dependencies [d9e908e]
- Updated dependencies [979e301]
- Updated dependencies [15781f0]
- Updated dependencies [be820c4]
- Updated dependencies [d9e908e]
  - fumadocs-core@14.0.0

## 1.1.4

### Patch Changes

- 0c251e5: Bump deps
- Updated dependencies [7dabbc1]
- Updated dependencies [0c251e5]
- Updated dependencies [3b56170]
  - fumadocs-core@13.4.2

## 1.1.3

### Patch Changes

- dfd8ac4: Fix type errors

## 1.1.2

### Patch Changes

- 758013f: Use Fumadocs Remark Image instead of `rehype-img-size`
- Updated dependencies [36b771b]
- Updated dependencies [61b91fa]
  - fumadocs-core@13.2.2

## 1.1.1

### Patch Changes

- c7aa090: Improve Fumadocs OpenAPI support
- Updated dependencies [17fa173]
  - fumadocs-core@13.2.1

## 1.1.0

### Minor Changes

- bc80ce3: Support dynamic resolving plugins

### Patch Changes

- Updated dependencies [fccdfdb]
- Updated dependencies [2ffd5ea]
  - fumadocs-core@12.5.4

## 1.0.3

### Patch Changes

- 6e9d4bf: Add `icon` and `root` fields to meta schema
- 2db6172: Add `cwd` option by default

## 1.0.2

### Patch Changes

- dd1e4f3: Change type definitions of built-in schemas
  - fumadocs-core@12.4.1

## 1.0.1

### Patch Changes

- 8efc775: Fix Content Collections compatibility
  - fumadocs-core@12.4.0

## 1.0.0

### Major Changes

- a25b3d1: Support Content Collections integration
`````

## File: packages/content-collections/README.md
`````markdown
# Fumadocs Content Collections

The Content Collections adapter for Fumadocs.
`````

## File: packages/core/test/fixtures/rehype-toc.md
`````markdown
# Heading 1

Some text here

## Heading 2

Some text here

### Heading 3

Some text here

### Custom heading id [#hello-world]

Some text here

### math $$C_L$$

Some text here

### Custom heading id hello-world]

Some text here

### `code` here
`````

## File: packages/core/test/fixtures/remark-admonition.md
`````markdown
:::tip

Hello World

:::

:::warn[This is Title]

Warning **this**

:::
`````

## File: packages/core/test/fixtures/remark-admonition.output.mdx
`````
<Callout type="info">
  Hello World
</Callout>

<Callout type="warn" title="This is Title">
  Warning **this**
</Callout>
`````

## File: packages/core/test/fixtures/remark-heading.md
`````markdown
# Heading 1

Some text here

## Heading 2

Some text here

### Heading 3

Some text here

### Custom heading id [#hello-world]

Some text here

### Custom heading id [#hello-2]

Some text here

### Custom heading id hello-world]

Some text here

### `code` here

hi
`````

## File: packages/core/test/fixtures/remark-image-public-dir.md
`````markdown
![External](/237/200/300)
`````

## File: packages/core/test/fixtures/remark-image-public-dir.output.mdx
`````
<img alt="External" src="/237/200/300" width="200" height="300" />
`````

## File: packages/core/test/fixtures/remark-image-without-import.output.mdx
`````
<img alt="Test" src="./test.png" width="1299" height="731" />

<img alt="External" src="https://fumadocs.dev/banner.png" width="1200" height="630" />
`````

## File: packages/core/test/fixtures/remark-image.md
`````markdown
![Test](./test.png)

![External](https://fumadocs.dev/banner.png)
`````

## File: packages/core/test/fixtures/remark-steps.md
`````markdown
# Hello

## 1. First

content

### Little Tip

content

## 2. Second

content

## 1. Third

content

## Ended

content

# 1. Big: First

content

# 2. Big: Second

content
`````

## File: packages/core/test/fixtures/remark-steps.output.md
`````markdown
# Hello

<div className="fd-steps">
  <div className="fd-step">
    ## First

    content

    ### Little Tip

    content
  </div>

  <div className="fd-step">
    ## Second

    content
  </div>

  <div className="fd-step">
    ## Third

    content
  </div>
</div>

## Ended

content

<div className="fd-steps">
  <div className="fd-step">
    # Big: First

    content
  </div>

  <div className="fd-step">
    # Big: Second

    content
  </div>
</div>
`````

## File: packages/core/test/fixtures/remark-structure.md
`````markdown
# Heading 1

Some text here

## Heading 2

Some text here

### Heading 3

| Name        | Description |
| ----------- | ----------- |
| Hello World | Goodbye     |

```ts
console.log('Not indexed');
```
`````

## File: packages/core/CHANGELOG.md
`````markdown
# next-docs-zeta

## 15.6.5

### Patch Changes

- 658fa96: Support custom options for error handling for `remark-image`

## 15.6.4

## 15.6.3

## 15.6.2

## 15.6.1

### Patch Changes

- 1a902ff: Fix static export map

## 15.6.0

### Minor Changes

- f8d1709: **Redesigned Codeblock Tabs**

  Instead of relying on `Tabs` component, it supports a dedicated tabs component for codeblocks:

  ```tsx
  <CodeBlockTabs>
    <CodeBlockTabsList>
      <CodeBlockTabsTrigger value="value">Name</CodeBlockTabsTrigger>
    </CodeBlockTabsList>
    <CodeBlockTab value="value" asChild>
      <CodeBlock>...</CodeBlock>
    </CodeBlockTab>
  </CodeBlockTabs>
  ```

  The old usage is not deprecated, you can still use them while Fumadocs' remark plugins will generate codeblock tabs using the new way.

### Patch Changes

- d0f8a15: Enable `remarkNpm` by default, replace `remarkInstall` with it.
- 84918b8: Support passing `tag` to search client/server as string array

## 15.5.5

### Patch Changes

- 0d3f76b: Fix wrong indexing of file system

## 15.5.4

### Patch Changes

- 35c3c0b: Support handling duplicated slugs and conflicts such as `dir/index.mdx` vs `dir.mdx`

## 15.5.3

### Patch Changes

- 7d1ac21: hotfix paths not being normalized on Windows

## 15.5.2

### Patch Changes

- 7a45921: Add `absolutePath` and `path` properties to pages, mark `file` as deprecated
- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos

## 15.5.1

### Patch Changes

- b4916d2: Move `hide-if-empty` component to Fumadocs Core
- 8738b9c: Always encode generated slugs for non-ASCII characters in `loader()`
- a66886b: **Deprecate other parameters for `useDocsSearch()`**

  The new usage passes options to a single object, improving the readability:

  ```ts
  import { useDocsSearch } from 'fumadocs-core/search/client';

  const { search, setSearch, query } = useDocsSearch({
    type: 'fetch',
    locale: 'optional',
    tag: 'optional',
    delayMs: 100,
    allowEmpty: false,
  });
  ```

## 15.5.0

## 15.4.2

### Patch Changes

- 0ab6c7f: Improve performance by using shallow compare on `useOnChange` by default

## 15.4.1

## 15.4.0

### Minor Changes

- 961b67e: **Bump algolia search to v5**

  This also introduced changes to some APIs since `algoliasearch` v4 and v5 has many differences.

  Now we highly recommend to pass an index name to `sync()`:

  ```ts
  import { algoliasearch } from 'algoliasearch';
  import { sync } from 'fumadocs-core/search/algolia';
  const client = algoliasearch('id', 'key');

  void sync(client, {
    indexName: 'document',
    documents: records,
  });
  ```

  For search client, pass them to `searchOptions`:

  ```tsx
  'use client';

  import { liteClient } from 'algoliasearch/lite';
  import type { SharedProps } from 'fumadocs-ui/components/dialog/search';
  import SearchDialog from 'fumadocs-ui/components/dialog/search-algolia';

  const client = liteClient(appId, apiKey);

  export default function CustomSearchDialog(props: SharedProps) {
    return (
      <SearchDialog
        searchOptions={{
          client,
          indexName: 'document',
        }}
        {...props}
        showAlgolia
      />
    );
  }
  ```

### Patch Changes

- 1b999eb: Introduce `<Markdown />` component
- 7d78bc5: Improve `createRelativeLink` and `getPageByHref` for i18n usage

## 15.3.4

## 15.3.3

### Patch Changes

- 4ae7b4a: Support MDX in codeblock tab value

## 15.3.2

### Patch Changes

- c25d678: Support Shiki focus notation transformer by default

## 15.3.1

### Patch Changes

- 3372792: Support line numbers in codeblock

## 15.3.0

### Patch Changes

- c05dc03: Improve error message of remark image

## 15.2.15

### Patch Changes

- 50db874: Remove placeholder space for codeblocks
- 79e75c3: Improve default MDX attribute indexing strategy for `remarkStructure`

## 15.2.14

### Patch Changes

- 6ea1718: Fix type inference for `pageTree.attachFile` in `loader()`

## 15.2.13

## 15.2.12

### Patch Changes

- acff667: **Deprecate `createFromSource(source, pageToIndex, options)`**

  Migrate:

  ```ts
  import { source } from '@/lib/source';
  import { createFromSource } from 'fumadocs-core/search/server';

  // from
  export const { GET } = createFromSource(
    source,
    (page) => ({
      title: page.data.title,
      description: page.data.description,
      url: page.url,
      id: page.url,
      structuredData: page.data.structuredData,
      // use your desired value, like page.slugs[0]
      tag: '<value>',
    }),
    {
      // options
    },
  );

  // to
  export const { GET } = createFromSource(source, {
    buildIndex(page) {
      return {
        title: page.data.title,
        description: page.data.description,
        url: page.url,
        id: page.url,
        structuredData: page.data.structuredData,
        // use your desired value, like page.slugs[0]
        tag: '<value>',
      };
    },
    // other options
  });
  ```

## 15.2.11

### Patch Changes

- 07cd690: Support separators without name

## 15.2.10

## 15.2.9

## 15.2.8

## 15.2.7

### Patch Changes

- ec85a6c: support more options on `remarkStructure`
- e1a61bf: Support `remarkSteps` plugin

## 15.2.6

### Patch Changes

- d49f9ae: Fix order of `<I18nProvider />`
- b07e98c: fix `loader().getNodePage()` returning undefined for other locales
- 3a4bd88: Fix wrong index files output in i18n page tree generation

## 15.2.5

### Patch Changes

- c66ed79: Fix `removeScrollOn` on sidebar primitive

## 15.2.4

### Patch Changes

- 1057957: Fix type problems on dynamic codeblock

## 15.2.3

## 15.2.2

### Patch Changes

- 0829544: deprecate `blockScrollingWidth` in favour of `removeScrollOn`

## 15.2.1

## 15.2.0

### Minor Changes

- 2fd325c: Enable `lazy` on `rehypeCode` by default
- a7cf4fa: Support other frameworks via `FrameworkProvider`

## 15.1.3

### Patch Changes

- b734f92: support `mdxJsxFlowElement` in `remarkStructure`

## 15.1.2

### Patch Changes

- 3f580c4: Support directory-based i18n routing

## 15.1.1

### Patch Changes

- c5add28: use internal store for Shiki highlighter instances
- f3cde4f: Support markdown files with default local code in file name
- 7c8a690: Improve file info interface
- b812457: Remove Next.js usage from search server

## 15.1.0

### Minor Changes

- f491f6f: Lazy build page tree by default
- f491f6f: Support `getPageByHref()` on loader API

### Patch Changes

- f491f6f: Fix `findNeighbour()` doesn't exclude other nodes of another root

## 15.0.18

## 15.0.17

### Patch Changes

- 72f79cf: Support Orama Cloud crawler index

## 15.0.16

## 15.0.15

### Patch Changes

- 9f6d39a: Fix peer deps
- 2035cb1: remove hook-level cache from `useDocsSearch()`

## 15.0.14

### Patch Changes

- 37dc0a6: Update `image-size` to v2
- 796cc5e: Upgrade to Orama v3
- 2cc0be5: Support to add custom serialization to `remarkStructure` via `data._string`

## 15.0.13

## 15.0.12

### Patch Changes

- 3534a10: Move `fumadocs-core` highlighting utils to `fumadocs-core/highlight` and `fumadocs-core/highlight/client`
- 93952db: Generate a `$id` attribute to page tree nodes

## 15.0.11

## 15.0.10

### Patch Changes

- d95c21f: add `initOrama` option to static client

## 15.0.9

## 15.0.8

## 15.0.7

### Patch Changes

- 5deaf40: Support icons in separators of `meta.json`

## 15.0.6

### Patch Changes

- 08236e1: Support custom toc settings in headings
- a06af26: Support pages without `title`

## 15.0.5

## 15.0.4

## 15.0.3

## 15.0.2

## 15.0.1

## 15.0.0

### Minor Changes

- 581f4a5: **Support code block tabs without hardcoding `<Tabs />` items**

  **migrate:** Use the `remarkCodeTab` plugin.

  **before:**

  ````mdx
  import { Tab, Tabs } from 'fumadocs-ui/components/tabs';

  <Tabs items={["Tab 1", "Tab 2"]}>

  ```ts tab
  console.log('A');
  ```

  ```ts tab
  console.log('B');
  ```

  </Tabs>
  ````

  **after:**

  ````mdx
  import { Tab, Tabs } from 'fumadocs-ui/components/tabs';

  ```ts tab="Tab 1"
  console.log('A');
  ```

  ```ts tab="Tab 2"
  console.log('B');
  ```
  ````

### Patch Changes

- 5b8cca8: Fix `remarkAdmonition` missing some types from Docusaurus
- a763058: Support reversed rest items in `meta.json`

## 14.7.7

## 14.7.6

### Patch Changes

- b9601fb: Update Shiki

## 14.7.5

### Patch Changes

- 777188b: [Page Tree Builder] Inline folders without children

## 14.7.4

### Patch Changes

- bb73a72: Fix search params being ignored in middleware redirection
- 69bd4fe: Support `source.getPageTree()` function

## 14.7.3

### Patch Changes

- 041f230: Support trailing slash

## 14.7.2

### Patch Changes

- 14b280c: Revert default i18n config

## 14.7.1

### Patch Changes

- 72dc093: Add chinese i18n configuration for Orama search if not specified

## 14.7.0

### Minor Changes

- 97ed36c: Remove defaults from `loader` and deprecate `rootDir` options

## 14.6.8

## 14.6.7

### Patch Changes

- 5474343: Export dynamic-link

## 14.6.6

## 14.6.5

### Patch Changes

- 969da26: Improve i18n api

## 14.6.4

### Patch Changes

- b71064a: Support remark plugins & vfile input on `getTableOfContents`

## 14.6.3

## 14.6.2

### Patch Changes

- 2357d40: Fix typings of `HighlightOptions`

## 14.6.1

## 14.6.0

### Minor Changes

- bebb16b: Add support for pre-rendering to `useShiki` hook
- 050b326: Support codeblock `tab` meta without value

### Patch Changes

- 4dfde6b: support additional `components` option of Orama search
- 4766292: Support React 19

## 14.5.6

### Patch Changes

- 9a18c14: Downgrade Orama to v2 to fix external tokenizers

## 14.5.5

## 14.5.4

## 14.5.3

## 14.5.2

## 14.5.1

## 14.5.0

## 14.4.2

## 14.4.1

## 14.4.0

## 14.3.1

## 14.3.0

## 14.2.1

### Patch Changes

- ca94bfd: Support sync usage of `getTableOfContents`

## 14.2.0

### Minor Changes

- e248a0f: Support Orama Cloud integration

## 14.1.1

### Patch Changes

- 1573d63: Support URL format `publicDir` in Remark Image plugin

## 14.1.0

### Minor Changes

- b262d99: bundle default Shiki transformers
- 90725c1: Support server-side `highlight` and client `useShiki` hook

### Patch Changes

- d6d290c: Upgrade Shiki
- 4a643ff: Prefer `peerDependenciesMeta` over `optionalDependencies`
- b262d99: Support JSX comment syntax on default Shiki transformers

## 14.0.2

## 14.0.1

## 14.0.0

### Major Changes

- e45bc67: **Remove deprecated `fumadocs-core/middleware` export**

  **migrate:** Use `fumadocs-core/i18n`.

- d9e908e: **Remove deprecated `languages` and `defaultLanguage` option from loader**

  **migrate:** Use I18n config API

- 9a0b09f: **Change usage of `useDocsSearch`**

  **why:** Allow static search

  **migrate:**

  Pass client option, it can be algolia, static, or fetch (default).

  ```ts
  import { useDocsSearch } from 'fumadocs-core/search/client';

  const { search, setSearch, query } = useDocsSearch({
    type: 'fetch',
    api: '/api/search', // optional
  });
  ```

- 9a0b09f: **Remove Algolia Search Client**

  **why:** Replace by the new search client

  **migrate:**

  ```ts
  import { useDocsSearch } from 'fumadocs-core/search/client';

  const { search, setSearch, query } = useDocsSearch({
    type: 'algolia',
    index,
    ...searchOptions,
  });
  ```

- 9a0b09f: **Refactor import path of `fumadocs-core/search-algolia/server` to `fumadocs-core/search/algolia`**
- d9e908e: Improved usage for `createI18nSearchAPI` (replaced `createI18nSearchAPIExperimental`)
- d9e908e: Replace `fumadocs-core/search/shared` with `fumadocs-core/server`

### Minor Changes

- d9e908e: Create search api from source (Support i18n without modifying search route handler)
- 367f4c3: Support referencing original page/meta from page tree nodes
- e1ee822: Support hast nodes in `toc` variable
- 979e301: Replace flexearch with Orama
- 979e301: Support static search (without server)
- d9e908e: Support creating metadata API from sources

### Patch Changes

- f949520: Support Shiki diff transformer
- e612f2a: Make compatible with Next.js 15
- 8ef00dc: Apply `hideLocale` to Source `getPage` APIs
- 15781f0: Fix breadcrumb empty when `includePage` isn't specified
- be820c4: Bump deps

## 13.4.10

### Patch Changes

- 6231ad3: fix(types): PageData & MetaData exactOptionalPropertyTypes compat

## 13.4.9

### Patch Changes

- 083f04a: Fix link items text

## 13.4.8

### Patch Changes

- 78e59e7: Support to add icons to link items in meta.json

## 13.4.7

### Patch Changes

- 6e1923e: Improve anchors observer

## 13.4.6

### Patch Changes

- afb697e: Fix Next.js 14.2.8 dynamic import problems
- daa66d2: Support generating static params automatically with Source API

## 13.4.5

## 13.4.4

### Patch Changes

- 729928e: Fix build error without JS engine

## 13.4.3

## 13.4.2

### Patch Changes

- 7dabbc1: Remark Image: Support relative imports
- 0c251e5: Bump deps
- 3b56170: Support to enable experiment Shiki JS engine

## 13.4.1

### Patch Changes

- 95dbba1: Scan table into search indexes by default

## 13.4.0

## 13.3.3

### Patch Changes

- f8cc167: Ignore numeric locale file name

## 13.3.2

### Patch Changes

- 0e0ef8c: Support headless search servers

## 13.3.1

## 13.3.0

### Minor Changes

- fd46eb6: Export new `createI18nSearchAPIExperimental` API for i18n config
- fd46eb6: Introduce `i18n` config for Core APIs
- fd46eb6: Deprecated `languages` and `defaultLanguage` option on Source API, replaced with `i18n` config
- fd46eb6: Move I18n middleware to `fumadocs-core/i18n`
- 9aae448: Support multiple toc active items
- c542561: Use cookie to store active locale on `always` mode

### Patch Changes

- 4916f84: Improve Source API performance

## 13.2.2

### Patch Changes

- 36b771b: Remark Image: Support relative import path
- 61b91fa: Improve Fumadocs OpenAPI support

## 13.2.1

### Patch Changes

- 17fa173: Remark Image: Support fetching image size of external urls

## 13.2.0

### Patch Changes

- 96c9dda: Change Heading scroll margins

## 13.1.0

### Patch Changes

- f280191: Page Tree Builder: Sort folders to bottom

## 13.0.7

### Patch Changes

- 37bbfff: Improve active anchor observer

## 13.0.6

## 13.0.5

### Patch Changes

- 2cf65f6: Support debounce value on algolia search client

## 13.0.4

### Patch Changes

- 5355391: Support indexing description field on documents

## 13.0.3

### Patch Changes

- 978342f: Type file system utilities (Note: This is an internal module, you're not supposed to reference it)

## 13.0.2

### Patch Changes

- 4819820: Page Tree Builder: Fallback to page icon when metadata doesn't exist

## 13.0.1

## 13.0.0

### Major Changes

- 09c3103: **Change usage of TOC component**

  **why:** Improve the flexibility of headless components

  **migrate:**

  Instead of

  ```tsx
  import * as Base from 'fumadocs-core/toc';

  return (
    <Base.TOCProvider>
      <Base.TOCItem />
    </Base.TOCProvider>
  );
  ```

  Use

  ```tsx
  import * as Base from 'fumadocs-core/toc';

  return (
    <Base.AnchorProvider>
      <Base.ScrollProvider>
        <Base.TOCItem />
        <Base.TOCItem />
      </Base.ScrollProvider>
    </Base.AnchorProvider>
  );
  ```

- b02eebf: **Remove deprecated option `defaultLang`**

  **why:** The default language feature has been supported by Shiki Rehype integration, you should use it directly.

  **migrate:** Rename to `defaultLanguage`.

### Minor Changes

- c714eaa: Support Remark Admonition plugin

## 12.5.6

## 12.5.5

## 12.5.4

### Patch Changes

- fccdfdb: Improve TOC Popover design
- 2ffd5ea: Support folder group on Page Tree Builder

## 12.5.3

## 12.5.2

### Patch Changes

- a5c34f0: Support specifying the url of root node when breadcrumbs have `includeRoot` enabled

## 12.5.1

## 12.5.0

### Minor Changes

- b9fa99d: Support `tag` facet field for Algolia Search Integration

### Patch Changes

- 525925b: Support including root folder into breadcrumbs

## 12.4.2

### Patch Changes

- 503e8e9: Support `keywords` API in advanced search

## 12.4.1

## 12.4.0

## 12.3.6

## 12.3.5

## 12.3.4

## 12.3.3

### Patch Changes

- 90d51cb: Fix problem with I18n middleware & language toggle

## 12.3.2

### Patch Changes

- ca7d0f4: Support resolving async search indexes

## 12.3.1

### Patch Changes

- cf852f6: Add configurable delayMs Parameter for Debounced Search Performance

## 12.3.0

### Minor Changes

- ce3c8ad: Page Tree Builder: Support `defaultLanguage` option
- ce3c8ad: Support hiding locale prefixes with I18n middleware

## 12.2.5

## 12.2.4

## 12.2.3

## 12.2.2

## 12.2.1

## 12.2.0

### Minor Changes

- b70ff06: Support `!name` to hide pages on `meta.json`

## 12.1.3

## 12.1.2

### Patch Changes

- b4856d1: Fix `createGetUrl` wrong locale position

## 12.1.1

### Patch Changes

- a39dbcb: Export `loadFiles` from Source API

## 12.1.0

### Minor Changes

- 0a377a9: **Support writing code blocks as a `<Tab />` element.**

  ````mdx
  import { Tabs } from 'fumadocs-ui/components/tabs';

  <Tabs items={["Tab 1", "Tab 2"]}>

  ```js tab="Tab 1"
  console.log('Hello');
  ```

  ```js tab="Tab 2"
  console.log('Hello');
  ```

  </Tabs>
  ````

  This is same as wrapping the code block in a `<Tab />` component.

- 0a377a9: **Pass the `icon` prop to code blocks as HTML instead of MDX attribute.**

  **why:** Only MDX flow elements support attributes with JSX value, like:

  ```mdx
  <Pre icon={<svg />}>...</Pre>
  ```

  As Shiki outputs hast elements, we have to convert the output of Shiki to a MDX flow element so that we can pass the `icon` property.

  Now, `rehype-code` passes a HTML string instead of JSX, and render it with `dangerouslySetInnerHTML`:

  ```mdx
  <Pre icon="<svg />">...</Pre>
  ```

  **migrate:** Not needed, it should work seamlessly.

## 12.0.7

## 12.0.6

### Patch Changes

- 7a29b79: Remove default language from `source.getLanguages`
- b0c1242: Support Next.js 15 cache behaviour in `getGithubLastEdit`

## 12.0.5

## 12.0.4

### Patch Changes

- 72dbaf1: Support `ReactNode` in page tree, table of contents and breadcrumb type definitions
- 51ca944: Support including separators in breadcrumbs

## 12.0.3

### Patch Changes

- 053609d: Rename `defaultLang` to `defaultLanguage`

## 12.0.2

## 12.0.1

## 12.0.0

### Major Changes

- 98430e9: **Remove `minWidth` deprecated option from `Sidebar` component.**

  **migrate:** Use `blockScrollingWidth` instead

### Minor Changes

- 57eb762: Support attaching custom properties during page tree builder process

### Patch Changes

- d88dfa6: Support attaching `id` property to page trees
- ba20694: Remark Headings: Support code syntax in headings

## 11.3.2

### Patch Changes

- 1b8e12b: Use `display: grid` for codeblocks

## 11.3.1

## 11.3.0

### Minor Changes

- 917d87f: Rename sidebar primitive `minWidth` prop to `blockScrollingWidth`

## 11.2.2

## 11.2.1

## 11.2.0

## 11.1.3

### Patch Changes

- 88008b1: Fix ESM compatibility problems in i18n middleware
- 944541a: Add dynamic page url according to locale
- 07a9312: Improve Search I18n utilities

## 11.1.2

## 11.1.1

### Patch Changes

- 8ef2b68: Bump deps
- 26f464d: Support relative paths in meta.json
- 26f464d: Support non-external link in meta.json

## 11.1.0

## 11.0.8

### Patch Changes

- 98258b5: Fix regex problems

## 11.0.7

### Patch Changes

- f7c2c5c: Fix custom heading ids conflicts with MDX syntax

## 11.0.6

### Patch Changes

- 5653d5d: Support customising heading id in headings
- 5653d5d: Support custom heading slugger

## 11.0.5

## 11.0.4

### Patch Changes

- 7b61b2f: Migrate `fumadocs-ui` to fully ESM, adding support for ESM `tailwind.config` file

## 11.0.3

## 11.0.2

## 11.0.1

## 11.0.0

### Major Changes

- 2d8df75: Remove `cwd` option from `remark-dynamic-content`

  why: Use `cwd` from vfile

  migrate: Pass the `cwd` option from remark instead

- 92cb12f: Simplify Source API virtual storage.

  why: Improve performance

  migrate:

  ```diff
  - storage.write('path.mdx', { type: 'page', ... })
  - storage.readPage('page')
  + storage.write('path.mdx', 'page', { ... })
  + storage.read('page', 'page')
  ```

  Transformers can now access file loader options.

  ```ts
  load({
    transformers: [
      ({ storage, options }) => {
        options.getUrl();
        options.getSlugs();
      },
    ],
  });
  ```

- f75287d: **Introduce `fumadocs-docgen` package.**

  Offer a better authoring experience for advanced use cases.
  - Move `remark-dynamic-content` and `remark-install` plugins to the new package `fumadocs-docgen`.
  - Support Typescript generator by default

  **Usage**

  Add the `remarkDocGen` plugin to your remark plugins.

  ```ts
  import { remarkDocGen, fileGenerator } from 'fumadocs-docgen';

  remark().use(remarkDocGen, { generators: [fileGenerator()] });
  ```

  Generate docs with code blocks.

  ````mdx
  ```json doc-gen:<generator>
  {
    // options
  }
  ```
  ````

  **Migrate**

  For `remarkDynamicContent`, enable `fileGenerator` and use this syntax:

  ````mdx
  ```json doc-gen:file
  {
    "file": "./path/to/my-file.txt"
  }
  ```
  ````

  For `remarkInstall`, it remains the same:

  ```ts
  import { remarkInstall } from 'fumadocs-docgen';
  ```

- 2d8df75: Remove support for `getTableOfContentsFromPortableText`

  why: Sanity integration should be provided by 3rd party integrations

  migrate: Use built-in sources, or write a custom implementation

## 10.1.3

### Patch Changes

- bbad52f: Support `bun` in `remark-install` plugin

## 10.1.2

## 10.1.1

### Patch Changes

- 779c599: Mark `getTableOfContentsFromPortableText` deprecated
- 0c01300: Fix remark-dynamic-content ignored code blocks
- 779c599: Support relative resolve path for remark-dynamic-content

## 10.1.0

## 10.0.5

### Patch Changes

- e47c62f: Improve remark plugin typings

## 10.0.4

## 10.0.3

### Patch Changes

- 6f321e5: Fix type errors of flexseach

## 10.0.2

### Patch Changes

- 10e099a: Remove deprecated options from `fumadocs-core/toc`

## 10.0.1

### Patch Changes

- c9b7763: Update to Next.js 14.1.0
- 0e78dc8: Support customising search API URL
- d8483a8: Remove undefined values from page tree

## 10.0.0

### Major Changes

- 321d1e1f: **Move Typescript integrations to `fumadocs-typescript`**

  why: It is now a stable feature

  migrate: Use `fumadocs-typescript` instead.

  ```diff
  - import { AutoTypeTable } from "fumadocs-ui/components/auto-type-table"
  + import { AutoTypeTable } from "fumadocs-typescript/ui"
  ```

### Minor Changes

- b5d16938: Support external link in `pages` property

## 9.1.0

### Minor Changes

- 909b0e35: Support duplicated names with meta and page files
- 1c388ca5: Support `defaultOpen` for folder nodes

### Patch Changes

- 691f12aa: Source API: Support relative paths as root directory

## 9.0.0

## 8.3.0

## 8.2.0

### Minor Changes

- 5c24659: Support code block icons

## 8.1.1

## 8.1.0

### Minor Changes

- eb028b4: Migrate to shiki
- 054ec60: Support generating docs for Typescript file

### Patch Changes

- 6c5a39a: Rename Git repository to `fumadocs`

## 8.0.0

### Major Changes

- 2ea9437: **Migrate to rehype-shikiji**
  - Dropped support for inline code syntax highlighting
  - Use notation-based word/line highlighting instead of meta string

  Before:

  ````md
  ```ts /config/ {1}
  const config = 'Hello';

  something.call(config);
  ```
  ````

  After:

  ````md
  ```ts
  // [!code word:config]
  const config = 'Hello'; // [!code highlight]

  something.call(config);
  ```
  ````

  Read the docs of Shikiji for more information.

- cdff313: **Separate Contentlayer integration into another package**

  why: As Fumadocs MDX is the preferred default source, Contentlayer should be optional.

  migrate:

  Install `fumadocs-contentlayer`.

  ```diff
  - import { createContentlayerSource } from "fumadocs-core/contentlayer"
  + import { createContentlayerSource } from "fumadocs-contentlayer"

  - import { createConfig } from "fumadocs-core/contentlayer/configuration"
  + import { createConfig } from "fumadocs-contentlayer/configuration"
  ```

- 2b11c20: **Rename to Fumadocs**

  `next-docs-zeta` -> `fumadocs-core`

  `next-docs-ui` -> `fumadocs-ui`

  `next-docs-mdx` -> `fumadocs-mdx`

  `@fuma-docs/openapi` -> `fumadocs-openapi`

  `create-next-docs-app` -> `create-fumadocs-app`

### Minor Changes

- 1a346a1: Add `remark-image` plugin that converts relative image urls into static image imports (Inspired by Nextra)

## 7.1.2

## 7.1.1

## 7.1.0

## 7.0.0

### Major Changes

- 9929c5b: **Migrate Contentlayer Integration to Source API**

  `createContentlayer` is now replaced by `createContentlayerSource`.

  You should configure base URL and root directory in the loader instead of Contentlayer configuration.

  It's no longer encouraged to access `allDocs` directly because they will not include `url` property anymore. Please consider `getPages` instead.

  ```ts
  import { allDocs, allMeta } from 'contentlayer/generated';
  import { createContentlayerSource } from 'next-docs-zeta/contentlayer';
  import { loader } from 'next-docs-zeta/source';

  export const { getPage, pageTree, getPages } = loader({
    baseUrl: '/docs',
    rootDir: 'docs',
    source: createContentlayerSource(allMeta, allDocs),
  });
  ```

  The interface is very similar, but you can only access Contentlayer properties from `page.data`.

  ```diff
  - <Content code={page.body.code} />
  + <Content code={page.data.body.code} />
  ```

- 9929c5b: **Source API**

  To reduce boilerplate, the Source API is now released to handle File-system based files.

  Thanks to this, you don't have to deal with the inconsistent behaviours between different content sources anymore.

  The interface is now unified, you can easily plug in a content source.

  ```ts
  import { map } from '@/.map';
  import { createMDXSource } from 'next-docs-mdx';
  import { loader } from 'next-docs-zeta/source';

  export const { getPage, getPages, pageTree } = loader({
    baseUrl: '/docs',
    rootDir: 'docs',
    source: createMDXSource(map),
  });
  ```

  **Page Tree Builder API is removed in favor of this**

- 49201be: **Change `remarkToc` to `remarkHeading`**

  The previous `remarkToc` plugin only extracts table of contents from documents, now it also adds the `id` property to all heading elements.

  ```diff
  - import { remarkToc } from "next-docs-zeta/mdx-plugins"
  + import { remarkHeading } from "next-docs-zeta/mdx-plugins"
  ```

- 4c1334e: **Improve `createI18nMiddleware` function**

  Now, you can export the middleware directly without a wrapper.

  From:

  ```ts
  export default function middleware(request: NextRequest) {
    return createI18nMiddleware(...);
  }
  ```

  To:

  ```ts
  export default createI18nMiddleware({
    defaultLanguage,
    languages,
  });
  ```

### Minor Changes

- 338ea98: **Export `create` function for Contentlayer configuration**

  If you want to include other document types, or override the output configuration, the `create` function can return the fields and document types you need.

  ```ts
  import { create } from 'next-docs-zeta/contentlayer/configuration';

  const config = create(options);

  export default {
    contentDirPath: config.contentDirPath,
    documentTypes: [config.Docs, config.Meta],
    mdx: config.mdx,
  };
  ```

- 9929c5b: **Support multiple page tree roots**

  You can specify a `root` property in `meta.json`, the nearest root folder will be used as the root of page tree instead.

  ```json
  {
    "title": "Hello World",
    "root": true
  }
  ```

## 6.1.0

### Minor Changes

- f39ae40: **Forward ref to `Link` and `DynamicLink` component**

  **Legacy import name `SafeLink` is now removed**

  ```diff
  - import { SafeLink } from "next-docs-zeta/link"
  + import Link from "next-docs-zeta/link"
  ```

## 6.0.2

## 6.0.1

## 6.0.0

### Major Changes

- 9ef047d: **Pre-bundle page urls into raw pages.**

  This means you don't need `getPageUrl` anymore for built-in adapters, including `next-docs-mdx` and Contentlayer. It is now replaced by the `url` property from the pages array provided by your adapter.

  Due to this change, your old configuration might not continues to work.

  ```diff
  import { fromMap } from 'next-docs-mdx/map'

  fromMap({
  -  slugs: ...
  +  getSlugs: ...
  })
  ```

  For Contentlayer, the `getUrl` option is now moved to `createConfig`.

## 5.0.0

### Minor Changes

- de44efe: Migrate to Shikiji
- de44efe: Support code highlighting options

## 4.0.9

### Patch Changes

- a883009: Fix empty extracted paragraphs in `remark-structure`

## 4.0.8

### Patch Changes

- e0c5c96: Make ESM only

## 4.0.7

### Patch Changes

- b9af5ed: Update tsup & dependencies

## 4.0.6

### Patch Changes

- ff38f6e: Replace `getGitLastEditTime` with new `getGithubLastEdit` API

## 4.0.5

## 4.0.4

## 4.0.3

### Patch Changes

- 0cc10cb: Support custom build page tree options

## 4.0.2

## 4.0.1

### Patch Changes

- 2da93d8: Support generating package install codeblocks automatically
- 01b23e2: Support Next.js 14

## 4.0.0

### Major Changes

- 6c4a782: Create `PageTreeBuilder` API

  The old `buildPageTree` function provided by 'next-docs-zeta/contentlayer' is
  now removed. Please use new API directly, or use the built-in
  `createContentlayer` utility instead.

  ```diff
  - import { buildPageTree } from 'next-docs-zeta/contentlayer'
  + import { createPageTreeBuilder } from 'next-docs-zeta/server'
  ```

### Minor Changes

- 6c4a782: Improve CommonJS/ESM compatibility

  Since this release, all server utilities will be CommonJS by default unless
  they have referenced ESM modules in the code. For instance,
  `next-docs-zeta/middleware` is now a CommonJS file. However, some modules,
  such as `next-docs-zeta/server` requires ESM-only package, hence, they remain
  a ESM file.

  Notice that the extension of client-side files is now `.js` instead of `.mjs`,
  but they're still ESM.

  **Why?**

  After migrating to `.mjs` Next.js config file, some imports stopped to work.
  The built-in Next.js bundler seems can't resolve these `next` imports in
  external packages, causing errors when modules have imported Next.js itself
  (e.g. `next/image`) in the code.

  By changing client-side files extension to `.mjs` and using CommonJS for
  server-side files, this error is solved.

## 4.0.0

### Major Changes

- 24245a3: Create `PageTreeBuilder` API

  The old `buildPageTree` function provided by 'next-docs-zeta/contentlayer' is
  now removed. Please use new API directly, or use the built-in
  `createContentlayer` utility instead.

  ```diff
  - import { buildPageTree } from 'next-docs-zeta/contentlayer'
  + import { createPageTreeBuilder } from 'next-docs-zeta/server'
  ```

### Minor Changes

- 678cd3d: Improve CommonJS/ESM compatibility

  Since this release, all server utilities will be CommonJS by default unless
  they have referenced ESM modules in the code. For instance,
  `next-docs-zeta/middleware` is now a CommonJS file. However, some modules,
  such as `next-docs-zeta/server` requires ESM-only package, hence, they remain
  a ESM file.

  Notice that the extension of client-side files is now `.js` instead of `.mjs`,
  but they're still ESM.

  **Why?**

  After migrating to `.mjs` Next.js config file, some imports stopped to work.
  The built-in Next.js bundler seems can't resolve these `next` imports in
  external packages, causing errors when modules have imported Next.js itself
  (e.g. `next/image`) in the code.

  By changing client-side files extension to `.mjs` and using CommonJS for
  server-side files, this error is solved.

## 3.0.0

### Major Changes

- a4a8120: Update search utilities import paths.

  Search Utilities in `next-docs-zeta/server` is now moved to
  `next-docs-zeta/search` and `next-docs-zeta/server-algolia`.

  Client-side Changes: `next-docs-zeta/search` -> `next-docs-zeta/search/client`
  `next-docs-zeta/search-algolia` -> `next-docs-zeta/search-algolia/client`

  If you're using Next Docs UI, make sure to import the correct path.

### Minor Changes

- 7a0690b: Export remark-toc and remark-structure MDX plugins

### Patch Changes

- 1043532: Type MDX Plugins

## 2.4.1

### Patch Changes

- dfc8b44: Remove tree root node from breadcrumb
- ef4d8cc: Expose props from SafeLink component

## 2.4.0

### Patch Changes

- 27ce871: Add missing shiki peer deps

## 2.3.3

### Patch Changes

- 634f7d3: Reduce dependencies
- eac081c: Update github urls & author name

## 2.3.2

## 2.3.1

## 2.3.0

### Minor Changes

- 6664178: Support algolia search
- a0f9911: Support `useAlgoliaSearch`
- 6664178: Improve search document structurize algorithm

## 2.2.0

## 2.1.2

### Patch Changes

- dfbbc17: Exclude index page from "..." operator
- 79227d8: Fix breadcrumb resolve index file

## 2.1.1

## 2.1.0

### Patch Changes

- a5a661e: Remove `item` prop from TOC items

## 2.0.3

## 2.0.2

### Patch Changes

- 74e5e85: Contentlayer: Support rest item in meta.json
- 72e9fdf: Contentlayer: Support extracting folder in meta.json

## 2.0.1

### Patch Changes

- 48c5256: Contentlayer: Sort pages by default

## 2.0.0

## 1.6.9

## 1.6.8

## 1.6.7

## 1.6.6

## 1.6.5

### Patch Changes

- 79abe84: Support collapsible sidebar

## 1.6.4

## 1.6.3

### Patch Changes

- 8d07003: Replace type of `TreeNode[]` with `PageTree`

## 1.6.2

## 1.6.1

### Patch Changes

- fc6279e: Support get last git edit time

## 1.6.0

### Minor Changes

- edb9930: Redesign Contentlayer adapter API

### Patch Changes

- cdd30d5: Create remark-dynamic-content plugin

## 1.5.3

### Patch Changes

- fa8d4cf: Update dependencies

## 1.5.2

## 1.5.1

## 1.5.0

### Minor Changes

- fb2abb3: Rewrite create search API & stabilize experimental Advanced Search

## 1.4.1

### Patch Changes

- Support better document search with `experimental_initSearchAPI`
- 3d92c92: Support custom computed fields in Contentlayer

## 1.4.0

### Patch Changes

- 0f106d9: Fix default sidebar element type

## 1.3.1

### Patch Changes

- ff05f5d: Support custom fields in Contentlayer configuration generator
- 7fb2b9e: Support custom page & folder icons

## 1.3.0

### Minor Changes

- 98226d9: Rewrite slugger and TOC utilities

## 1.2.1

### Patch Changes

- b15895f: Remove url prop from page tree folders

## 1.2.0

### Patch Changes

- 5f248fb: Support Auto Scroll in TOC for headless docs

## 1.1.4

### Patch Changes

- 496a6b0: Configure eslint + prettier

## 1.1.3

### Patch Changes

- 0998b1b: Support edge runtime middlewares

## 1.1.2

### Patch Changes

- Fix aria attributes

## 1.1.1

## 1.1.0

### Patch Changes

- 255fc92: Support finding neighbours of a page & Flatten page tree

## 1.0.0

### Major Changes

- 8e4a001: Rewrite Contentlayer tree builder + Support Context API

### Minor Changes

- 4fa45c0: Add support for dynamic hrefs and relative paths to `<SafeLink />`
  component
- 0983891: Add international Docs search

## 0.3.2

## 0.3.1

## 0.3.0

## 0.2.1

### Patch Changes

- 67cd8ab: Remove unused files in dist

## 0.2.0

### Minor Changes

- 5ff94af: Replace TOC data attribute `data-active` with `aria-selected`

### Patch Changes

- 5ff94af: Fix contentlayer parser bugs

## 0.1.0

### Minor Changes

- Add get toc utils for sanity (portable text)

## 0.0.2

### Patch Changes

- d909192: Fix several contentlayer scanner bugs
- e88eec8: Add README
`````

## File: packages/core/README.md
`````markdown
# Fumadocs Core

The core library for Fumadocs.

📘 Learn More: [Documentation](https://fumadocs.vercel.app)
`````

## File: packages/create-app/template/+next/content/docs/index.mdx
`````
---
title: Hello World
description: Your first document
---

Welcome to the docs! You can start writing documents in `/content/docs`.

## What is Next?

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>
`````

## File: packages/create-app/template/+next/content/docs/test.mdx
`````
---
title: Components
description: Components
---

## Code Block

```js
console.log('Hello World');
```

## Cards

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>
`````

## File: packages/create-app/template/+next/README.md
`````markdown
This is a Next.js application generated with
[Create Fumadocs](https://github.com/fuma-nama/fumadocs).

Run development server:

```bash
npm run dev
# or
pnpm dev
# or
yarn dev
```

Open http://localhost:3000 with your browser to see the result.

## Explore

In the project, you can see:

- `lib/source.ts`: Code for content source adapter, [`loader()`](https://fumadocs.dev/docs/headless/source-api) provides the interface to access your content.
- `app/layout.config.tsx`: Shared options for layouts, optional but preferred to keep.

| Route                     | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| `app/(home)`              | The route group for your landing page and other pages. |
| `app/docs`                | The documentation layout and pages.                    |
| `app/api/search/route.ts` | The Route Handler for search.                          |

## Learn More

To learn more about Next.js and Fumadocs, take a look at the following
resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js
  features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [Fumadocs](https://fumadocs.vercel.app) - learn about Fumadocs
`````

## File: packages/create-app/template/+next+fuma-docs-mdx/README.md
`````markdown
This is a Next.js application generated with
[Create Fumadocs](https://github.com/fuma-nama/fumadocs).

Run development server:

```bash
npm run dev
# or
pnpm dev
# or
yarn dev
```

Open http://localhost:3000 with your browser to see the result.

## Explore

In the project, you can see:

- `lib/source.ts`: Code for content source adapter, [`loader()`](https://fumadocs.dev/docs/headless/source-api) provides the interface to access your content.
- `app/layout.config.tsx`: Shared options for layouts, optional but preferred to keep.

| Route                     | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| `app/(home)`              | The route group for your landing page and other pages. |
| `app/docs`                | The documentation layout and pages.                    |
| `app/api/search/route.ts` | The Route Handler for search.                          |

### Fumadocs MDX

A `source.config.ts` config file has been included, you can customise different options like frontmatter schema.

Read the [Introduction](https://fumadocs.dev/docs/mdx) for further details.

## Learn More

To learn more about Next.js and Fumadocs, take a look at the following
resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js
  features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [Fumadocs](https://fumadocs.vercel.app) - learn about Fumadocs
`````

## File: packages/create-app/template/react-router/content/docs/index.mdx
`````
---
title: Hello World
description: |
  Your first `document`
  You'll love it!
---

Hey there! Fumadocs is the docs framework that also works on React Router!

## Heading

Hello World

<Cards>
  <Card title="Learn more about React Router" href="https://reactrouter.com" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

```ts
console.log('I love React!');
```

### Heading

#### Heading

| Head                            | Description                         |
| ------------------------------- | ----------------------------------- |
| `hello`                         | Hello World                         |
| very **important**              | Hey                                 |
| _Surprisingly_                  | Fumadocs                            |
| very long text that looks weird | hello world hello world hello world |
`````

## File: packages/create-app/template/react-router/content/docs/test.mdx
`````
---
title: Test
description: A document to test Fumadocs
---

Hey there!

## Cards

<Cards>
  <Card title="Learn more about Next.js" href="https://nextjs.org/docs" />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### CodeBlock

```js
console.log('Hello World');
```

#### List

- Hello
- World
`````

## File: packages/create-app/template/react-router/README.md
`````markdown
This is a React Router application generated with
[Create Fumadocs](https://github.com/fuma-nama/fumadocs).

Run development server:

```bash
npm run dev
# or
pnpm dev
# or
yarn dev
```
`````

## File: packages/create-app/template/tanstack-start/content/index.mdx
`````
---
title: Hello World
description: Your favourite docs framework.
icon: Rocket
---

Hey there! Fumadocs is a docs framework built for Next.js, but do you know it also works on Tanstack Start?

## Heading

Hello World!

<Cards>
  <Card
    title="Learn more about Tanstack Start"
    href="https://tanstack.com/start"
  />
  <Card title="Learn more about Fumadocs" href="https://fumadocs.vercel.app" />
</Cards>

### CodeBlock

```ts
console.log('Hello World');
```

#### Table

| Head                            | Description                         |
| ------------------------------- | ----------------------------------- |
| `hello`                         | Hello World                         |
| very **important**              | Hey                                 |
| _Surprisingly_                  | Fumadocs                            |
| very long text that looks weird | hello world hello world hello world |
`````

## File: packages/create-app/template/tanstack-start/content/test.mdx
`````
---
title: Test
description: This is another page
---

Hello World again!

## Installation

```npm
npm i fumadocs-core fumadocs-ui
```
`````

## File: packages/create-app/template/tanstack-start/README.md
`````markdown
This is a Tanstack Start application generated with
[Create Fumadocs](https://github.com/fuma-nama/fumadocs).

Run development server:

```bash
npm run dev
# or
pnpm dev
# or
yarn dev
```
`````

## File: packages/create-app/CHANGELOG.md
`````markdown
# create-next-docs-app

## 15.6.5

### Patch Changes

- 619806d: Fix Vite and Tanstack Router configuration warnings

## 15.6.4

### Patch Changes

- a375da3: support passing options
- a375da3: Update templates

## 15.6.3

## 15.6.2

## 15.6.1

## 15.6.0

## 15.5.5

## 15.5.4

## 15.5.3

## 15.5.2

## 15.5.1

## 15.5.0

## 15.4.2

## 15.4.1

## 15.4.0

## 15.3.4

### Patch Changes

- a6c909b: Removed unused devDependencies and migrated from `fast-glob` to `tinyglobby`

## 15.3.3

## 15.3.2

## 15.3.1

## 15.3.0

## 15.2.15

## 15.2.14

## 15.2.13

## 15.2.12

## 15.2.11

## 15.2.10

## 15.2.9

## 15.2.8

## 15.2.7

### Patch Changes

- b8485e1: Enable TypeScript declaration generation in tsup config

## 15.2.6

### Patch Changes

- e9f2b70: Allow code usage of `create()`

## 15.2.5

### Patch Changes

- 74c4bb1: enable turbopack by default
- 3aac8e0: Include `mdx-components.tsx` by default

## 15.2.4

## 15.2.3

## 15.2.2

## 15.2.1

## 15.2.0

### Patch Changes

- 372843d: Add React Router example
- d5193e7: improve install experience
- 372843d: Remove Tailwind CSS option, enable by default

## 15.1.3

## 15.1.2

## 15.1.1

## 15.1.0

## 15.0.18

## 15.0.17

## 15.0.16

### Patch Changes

- 91c8568: add comments to generated template

## 15.0.15

## 15.0.14

## 15.0.13

## 15.0.12

## 15.0.11

## 15.0.10

## 15.0.9

## 15.0.8

## 15.0.7

### Patch Changes

- b3c0ee8: Fix windows problems

## 15.0.6

### Patch Changes

- e9225e1: Support src directory config

## 15.0.5

## 15.0.4

### Patch Changes

- 4be74f6: Improve CLI

## 15.0.3

## 15.0.2

## 15.0.1

## 15.0.0

### Patch Changes

- a89d6e0: Support Fumadocs v15

## 14.7.7

## 14.7.6

## 14.7.5

## 14.7.4

## 14.7.3

## 14.7.2

## 14.7.1

## 14.7.0

## 14.6.8

## 14.6.7

## 14.6.6

## 14.6.5

## 14.6.4

## 14.6.3

## 14.6.2

## 14.6.1

## 14.6.0

## 14.5.6

## 14.5.5

## 14.5.4

## 14.5.3

## 14.5.2

## 14.5.1

## 14.5.0

## 14.4.2

## 14.4.1

## 14.4.0

## 14.3.1

## 14.3.0

### Patch Changes

- 46d9208: Add option for ESLint

## 14.2.1

## 14.2.0

## 14.1.1

## 14.1.0

## 14.0.2

## 14.0.1

## 14.0.0

## 13.4.10

## 13.4.9

## 13.4.8

## 13.4.7

### Patch Changes

- 6e1923e: Fix typos

## 13.4.6

### Patch Changes

- 9c2095e: Add home layout by default

## 13.4.5

## 13.4.4

## 13.4.3

### Patch Changes

- e409799: Fix typos

## 13.4.2

### Patch Changes

- 0c251e5: Bump deps

## 13.4.1

## 13.4.0

## 13.3.3

## 13.3.2

## 13.3.1

## 13.3.0

### Patch Changes

- 5ed3e08: Install the @types/node package

## 13.2.2

## 13.2.1

## 13.2.0

### Patch Changes

- 70f15af: Support to initialize git repo

## 13.1.0

## 13.0.7

## 13.0.6

## 13.0.5

## 13.0.4

## 13.0.3

## 13.0.2

## 13.0.1

### Patch Changes

- 1f1989e: Update versions

## 13.0.0

## 12.5.6

## 12.5.5

## 12.5.4

## 12.5.3

## 12.5.2

## 12.5.1

## 12.5.0

## 12.4.2

## 12.4.1

### Patch Changes

- dd1e4f3: Change type definitions of built-in schemas

## 12.4.0

### Patch Changes

- 8efc775: Fix Content Collections compatibility

## 12.3.6

## 12.3.5

### Patch Changes

- ff7bcc4: Replace `contentlayer` with `content-collections`

## 12.3.4

## 12.3.3

## 12.3.2

## 12.3.1

## 12.3.0

## 12.2.5

## 12.2.4

### Patch Changes

- 7a326d3: Fix missing imports from template

## 12.2.3

## 12.2.2

## 12.2.1

## 12.2.0

### Patch Changes

- 7601b35: Move DocsLayout options to layout.config.tsx

## 12.1.3

## 12.1.2

## 12.1.1

## 12.1.0

## 12.0.7

## 12.0.6

## 12.0.5

## 12.0.4

## 12.0.3

## 12.0.2

## 12.0.1

## 12.0.0

### Patch Changes

- c7b0e23: Add `layout.config.tsx` for sharing layout options

## 11.3.2

## 11.3.1

## 11.3.0

## 11.2.2

## 11.2.1

## 11.2.0

## 11.1.3

## 11.1.2

## 11.1.1

### Patch Changes

- 8ef2b68: Bump deps

## 11.1.0

## 11.0.8

## 11.0.7

## 11.0.6

## 11.0.5

## 11.0.4

## 11.0.3

## 11.0.2

## 11.0.1

## 11.0.0

## 10.1.3

## 10.1.2

## 10.1.1

## 10.1.0

## 10.0.5

## 10.0.4

### Patch Changes

- c28c80f: Bump dependencies in templates

## 10.0.3

## 10.0.2

## 10.0.1

## 10.0.0

## 9.1.0

## 9.0.0

### Patch Changes

- c1e65b72: Fix typos

## 8.3.0

## 8.2.0

## 8.1.1

## 8.1.0

### Patch Changes

- 6c5a39a: Rename Git repository to `fumadocs`

## 8.0.0

### Major Changes

- 2b11c20: **Rename to Fumadocs**

  `next-docs-zeta` -> `fumadocs-core`

  `next-docs-ui` -> `fumadocs-ui`

  `next-docs-mdx` -> `fumadocs-mdx`

  `@fuma-docs/openapi` -> `fumadocs-openapi`

  `create-next-docs-app` -> `create-fumadocs-app`

## 7.1.2

### Patch Changes

- b836055: Remove deprecated usage from templates

## 7.1.1

### Patch Changes

- 65f71d4: Fix picocolors import errors

## 7.1.0

## 7.0.0

### Major Changes

- 579ecaa: **Support template for Tailwind CSS + Next Docs MDX**

## 6.1.0

### Patch Changes

- 65b7f30: Update examples
- 3e34d14: Sync version with next-docs

## 1.7.4

### Patch Changes

- 3840ad6: Update to 6.0.0

## 1.7.3

### Patch Changes

- b9af5ed: Update tsup & dependencies

## 1.7.2

### Patch Changes

- 0686061: Restrict node.js environment

## 1.7.1

### Patch Changes

- 955a575: Fix CLI errors

## 1.7.0

### Minor Changes

- 334a960: Support installing packages automatically

### Patch Changes

- 334a960: Support relative paths as project name (e.g. ".")

## 1.6.2

### Patch Changes

- 94075b8: Fix type errors in examples

## 1.6.1

### Patch Changes

- 01b23e2: Support Next.js 14

## 1.6.0

### Minor Changes

- c36c395: Support Next Docs MDX example

## 1.5.28

### Patch Changes

- 33914b0: Update Examples

## 1.5.27

### Patch Changes

- 45a4571: Update Examples

## 1.5.26

### Patch Changes

- 65eee50: Use async fs APIs
- eac081c: Update github urls & author name

## 1.5.25

### Patch Changes

- cbea678: Update Examples

## 1.5.24

### Patch Changes

- cd5fb12: Update Examples

## 1.5.23

### Patch Changes

- 379033d: Update Examples

## 1.5.22

### Patch Changes

- 7560a42: Update Examples

## 1.5.21

### Patch Changes

- d70fb5b: Update Examples

## 1.5.20

### Patch Changes

- Update Examples

## 1.5.18

### Patch Changes

- Update examples

## 1.5.17

### Patch Changes

- Update examples

## 1.5.16

### Patch Changes

- Update examples

## 1.5.15

### Patch Changes

- Update examples

## 1.5.14

### Patch Changes

- Update examples

## 1.5.13

### Patch Changes

- Update example

## 1.5.12

### Patch Changes

- Update examples

## 1.5.11

### Patch Changes

- Update examples

## 1.5.10

### Patch Changes

- Update examples

## 1.5.9

### Patch Changes

- Update dependencies

## 1.5.8

### Patch Changes

- 8f6f3c6: Update examples

## 1.5.7

### Patch Changes

- Update examples

## 1.5.6

### Patch Changes

- ebfdb88: Fix default warnings

## 1.5.5

### Patch Changes

- 3b0f469: Generate .gitignore file by default
- fa8d4cf: Update dependencies

## 1.5.4

### Patch Changes

- Update next docs

## 1.5.3

### Patch Changes

- Update next docs

## 1.5.2

### Patch Changes

- 9abd9de: Fix create-next-docs-app version conflicts

## 1.5.0

### Minor Changes

- Create create-next-docs-app CLI
`````

## File: packages/create-app/README.md
`````markdown
# Create Fumadocs App

A CLI tool to create new Next.js documentation sites with Fumadocs.

```bash
npx create-fumadocs-app
#or
pnpm create fumadocs-app
#or
yarn create fumadocs-app
```
`````

## File: packages/doc-gen/test/fixtures/file-gen.md
`````markdown
## Hello World

```json doc-gen:file
{
  "file": "./fixtures/sample.txt"
}
```

## Code Block

```json doc-gen:file
{
  "file": "./fixtures/sample.ts",
  "codeblock": true
}
```

## Code Block with config

```json doc-gen:file
{
  "file": "./fixtures/sample.txt",
  "codeblock": {
    "lang": "md",
    "meta": "title=\"Hello World\""
  }
}
```
`````

## File: packages/doc-gen/test/fixtures/file-gen.output.md
`````markdown
## Hello World

Hello World

This is some text

## Code Block

```ts
export interface Test1 {
  name: string;
  description: string;
  isGood: boolean;
}
```

## Code Block with config

```md title="Hello World"
Hello World

This is some text
```
`````

## File: packages/doc-gen/test/fixtures/file-gen.relative.md
`````markdown
## Hello World

```json doc-gen:file
{
  "file": "./sample.txt",
  "codeblock": true
}
```
`````

## File: packages/doc-gen/test/fixtures/file-gen.relative.output.md
`````markdown
## Hello World

```txt
Hello World

This is some text
```
`````

## File: packages/doc-gen/test/fixtures/remark-install-persist.md
`````markdown
```package-install
npm i next -D
```
`````

## File: packages/doc-gen/test/fixtures/remark-install.md
`````markdown
```package-install
next
```
`````

## File: packages/doc-gen/test/fixtures/remark-show.mdx
`````
<show on={true}>

    ## Hello World

    ```ts
    console.log("Goodbye")
    ```

</show>

<show on={() => test()}>

    ## Test

    ```ts
    console.log("Test")
    ```

</show>
`````

## File: packages/doc-gen/test/fixtures/sample.txt
`````
Hello World

This is some text
`````

## File: packages/doc-gen/test/fixtures/ts2js.md
`````markdown
```tsx ts2js
import { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  const v: string = 'hello world' as any;

  return (
    <div>
      {children} {v}
    </div>
  );
}
```
`````

## File: packages/doc-gen/CHANGELOG.md
`````markdown
# fumadocs-docgen

## 2.1.0

### Minor Changes

- d0f8a15: Enable `remarkNpm` by default, replace `remarkInstall` with it.
- f8d1709: **Redesigned Codeblock Tabs**

  Instead of relying on `Tabs` component, it supports a dedicated tabs component for codeblocks:

  ```tsx
  <CodeBlockTabs>
    <CodeBlockTabsList>
      <CodeBlockTabsTrigger value="value">Name</CodeBlockTabsTrigger>
    </CodeBlockTabsList>
    <CodeBlockTab value="value" asChild>
      <CodeBlock>...</CodeBlock>
    </CodeBlockTab>
  </CodeBlockTabs>
  ```

  The old usage is not deprecated, you can still use them while Fumadocs' remark plugins will generate codeblock tabs using the new way.

## 2.0.1

### Patch Changes

- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos

## 2.0.0

### Major Changes

- 4642a86: **Remove `typescriptGenerator` from `fumadocs-docgen`**

  **why:** Move dedicated parts to `fumadocs-typescript`, so all docs generation features for TypeScript can be put together in a single module.

  **migrate:** Use `fumadocs-typescript` We made a new `remarkAutoTypeTable` remark plugin generating the type table but with a different syntax:

  ```mdx
  <auto-type-table path="./my-file.ts" name="MyInterface" />
  ```

  Instead of:

  ````mdx
  ```json doc-gen:typescript
  {
    "file": "./my-file.ts",
    "name": "MyInterface"
  }
  ```
  ````

- 4642a86: **Move `remarkTypeScriptToJavaScript` plugin to `fumadocs-docgen/remark-ts2js`.**

  **why:** Fix existing problems with `oxc-transform`.

  **migrate:**

  Import it like:

  ```ts
  import { remarkTypeScriptToJavaScript } from 'fumadocs-docgen/remark-ts2js';
  ```

  instead of importing from `fumadocs-docgen`.

## 1.3.8

### Patch Changes

- Updated dependencies [7608f4e]
  - fumadocs-typescript@3.0.4

## 1.3.7

### Patch Changes

- 260128f: Add `remarkShow` plugin
  - fumadocs-typescript@3.0.3

## 1.3.6

### Patch Changes

- a8e9e1f: Bump deps
  - fumadocs-typescript@3.0.3

## 1.3.5

### Patch Changes

- b9601fb: Update Shiki
- Updated dependencies [b9601fb]
  - fumadocs-typescript@3.0.3

## 1.3.4

### Patch Changes

- 6d3c7d2: Use `oxc` for `ts2js` remark plugins
  - fumadocs-typescript@3.0.2

## 1.3.3

### Patch Changes

- 4ab0de6: Support TS2JS remark plugin [experimental]
  - fumadocs-typescript@3.0.2

## 1.3.2

### Patch Changes

- Updated dependencies [c042eb7]
  - fumadocs-typescript@3.0.2

## 1.3.1

### Patch Changes

- Updated dependencies [d6d290c]
  - fumadocs-typescript@3.0.1

## 1.3.0

### Minor Changes

- f9adba6: Support inline type syntax in `AutoTypeTable` `type` prop

### Patch Changes

- be820c4: Bump deps
- Updated dependencies [f9adba6]
- Updated dependencies [f9adba6]
- Updated dependencies [f9adba6]
- Updated dependencies [be820c4]
  - fumadocs-typescript@3.0.0

## 1.2.0

### Minor Changes

- 3a2c837: Improve caching

### Patch Changes

- 0c251e5: Bump deps
- Updated dependencies [0c251e5]
- Updated dependencies [3a2c837]
  - fumadocs-typescript@2.1.0

## 1.1.0

### Minor Changes

- 979896f: Support generating Tabs with `persist` enabled (Fumadocs UI only)

### Patch Changes

- fumadocs-typescript@2.0.1

## 1.0.2

### Patch Changes

- 8ef2b68: Bump deps
- Updated dependencies [8ef2b68]
  - fumadocs-typescript@2.0.1

## 1.0.1

### Patch Changes

- Updated dependencies [f75287d]
  - fumadocs-typescript@2.0.0
`````

## File: packages/doc-gen/README.md
`````markdown
# Fumadocs Doc Gen

Remark plugins & Docs Generator utilities.
`````

## File: packages/mdx/test/fixtures/index.mdx
`````
# Hello World
`````

## File: packages/mdx/CHANGELOG.md
`````markdown
# next-docs-mdx

## 11.7.0

### Minor Changes

- f8a58c6: Support `preset: minimal` to disable Fumadocs specific defaults
- e5cfa27: Stabilize Vite plugin support

### Patch Changes

- Updated dependencies [658fa96]
- Updated dependencies [f8a58c6]
  - fumadocs-core@15.6.5
  - @fumadocs/mdx-remote@1.4.0

## 11.6.11

### Patch Changes

- 73e07a5: bump zod to v4

## 11.6.10

### Patch Changes

- d0f8a15: Enable `remarkNpm` by default, replace `remarkInstall` with it.
- Updated dependencies [d0f8a15]
- Updated dependencies [84918b8]
- Updated dependencies [f8d1709]
  - fumadocs-core@15.6.0
  - @fumadocs/mdx-remote@1.3.4

## 11.6.9

### Patch Changes

- cd86f58: Hotfix Windows EOL being ignored
- Updated dependencies [7d1ac21]
  - fumadocs-core@15.5.3

## 11.6.8

### Patch Changes

- 7a45921: Add `absolutePath` and `path` properties to pages, mark `file` as deprecated
- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos
- 14e267b: Use custom util to parse frontmatter
- Updated dependencies [7a45921]
- Updated dependencies [1b7bc4b]
  - fumadocs-core@15.5.2
  - @fumadocs/mdx-remote@1.3.3

## 11.6.7

### Patch Changes

- a5c283f: Support `outDir` option on `createMDX()`
- Updated dependencies [b4916d2]
- Updated dependencies [8738b9c]
- Updated dependencies [a66886b]
  - fumadocs-core@15.5.1

## 11.6.6

### Patch Changes

- cd42e78: Support last modified time on Async Mode
- Updated dependencies [1b999eb]
- Updated dependencies [961b67e]
- Updated dependencies [7d78bc5]
  - fumadocs-core@15.4.0

## 11.6.5

### Patch Changes

- a6c909b: Removed unused devDependencies and migrated from `fast-glob` to `tinyglobby`
- Updated dependencies [a6c909b]
  - @fumadocs/mdx-remote@1.3.2
  - fumadocs-core@15.3.4

## 11.6.4

### Patch Changes

- 4ae7b4a: Support MDX in codeblock tab value
- Updated dependencies [4ae7b4a]
  - @fumadocs/mdx-remote@1.3.1
  - fumadocs-core@15.3.3

## 11.6.3

### Patch Changes

- 4de7fe7: Fix `meta.{locale}` file being excluded from `defineDocs`
- Updated dependencies [c05dc03]
  - fumadocs-core@15.3.0

## 11.6.2

### Patch Changes

- 16c7566: Improve error handling logic on parsing meta entries
- 7b89faa: Add `page.data.content` to sync mode
  - fumadocs-core@15.2.13

## 11.6.1

### Patch Changes

- 434ccb2: Improve performance
  - fumadocs-core@15.2.9

## 11.6.0

### Minor Changes

- 7fcf612: Require Next.js 15.3.0 or above

### Patch Changes

- Updated dependencies [ec85a6c]
- Updated dependencies [e1a61bf]
  - fumadocs-core@15.2.7

## 11.5.8

### Patch Changes

- 6c5e47a: add default types for collection without schema
- Updated dependencies [1057957]
  - fumadocs-core@15.2.4

## 11.5.7

### Patch Changes

- 5163e92: Support reusing codeblocks in `<include>`
- Updated dependencies [c5add28]
- Updated dependencies [6493817]
- Updated dependencies [f3cde4f]
- Updated dependencies [7c8a690]
- Updated dependencies [b812457]
  - fumadocs-core@15.1.1
  - @fumadocs/mdx-remote@1.2.1

## 11.5.6

### Patch Changes

- 927ee8b: Fix hot reload
  - fumadocs-core@15.0.9

## 11.5.5

### Patch Changes

- e6df8aa: Improve performance
  - fumadocs-core@15.0.8

## 11.5.4

### Patch Changes

- fc5d7c0: Compile Meta files into inline JSON objects
- Updated dependencies [5deaf40]
  - fumadocs-core@15.0.7

## 11.5.3

### Patch Changes

- 65ae933: Fix dependencies

## 11.5.2

### Patch Changes

- c571417: Improve performance
- be3acf4: Improve types
  - fumadocs-core@15.0.5

## 11.5.1

### Patch Changes

- 3730739: Fix types errors

## 11.5.0

### Minor Changes

- 233a2d1: Support Standard Schema for collection `schema`
- 432c7bd: Support `defineDocs` without re-exporting `docs` and `meta` collections

### Patch Changes

- Updated dependencies [69f20cb]
  - @fumadocs/mdx-remote@1.2.0
  - fumadocs-core@15.0.3

## 11.4.1

### Patch Changes

- a8e9e1f: Bump deps
  - fumadocs-core@15.0.2

## 11.4.0

### Minor Changes

- 421166a: Improve performance, remove unused imports

### Patch Changes

- 421166a: Fix Fumadocs 14 compatibility issues
  - fumadocs-core@15.0.1

## 11.3.2

### Patch Changes

- a89d6e0: Support Fumadocs v15
- d6781cc: Fix incorrect line number with frontmatter on dev mode
- Updated dependencies [5b8cca8]
- Updated dependencies [a763058]
- Updated dependencies [581f4a5]
  - fumadocs-core@15.0.0

## 11.3.1

### Patch Changes

- 69bd4fe: Fix nested references for `<include />`
- Updated dependencies [bb73a72]
- Updated dependencies [69bd4fe]
  - fumadocs-core@14.7.4

## 11.3.0

### Minor Changes

- a4eb326: Deprecate `generateManifest` option: use a route handler to export build time information

### Patch Changes

- 7cc9f1f: Support CommonJs usage temporarily

## 11.2.3

### Patch Changes

- 0a5b08c: Fix alias imports
- Updated dependencies [72dc093]
  - fumadocs-core@14.7.1

## 11.2.2

### Patch Changes

- 97ed36c: Improve default settings
- Updated dependencies [97ed36c]
  - fumadocs-core@14.7.0

## 11.2.1

### Patch Changes

- 3445182: Fix `include` hot-reload issues
- Updated dependencies [b71064a]
  - fumadocs-core@14.6.4

## 11.2.0

### Minor Changes

- bd0a140: Support reusing content with `include` tag

### Patch Changes

- fumadocs-core@14.6.3

## 11.1.2

### Patch Changes

- fe36593: Fix global config types

## 11.1.1

### Patch Changes

- 164b9e6: Fix non-absolute `dir` option
- Updated dependencies [1573d63]
  - fumadocs-core@14.1.1

## 11.1.0

### Minor Changes

- 28a9c3c: Migrate loaders to ESM only

## 11.0.0

### Major Changes

- e094284: **Require Fumadocs v14**

### Patch Changes

- fumadocs-core@14.0.1

## 10.1.0

### Minor Changes

- 5cef1f1: Move `dir` option from `defineDocs`
- e1ee822: Support hast nodes in `toc` variable
- df9e0e1: Support `async` output mode

### Patch Changes

- 9a964ca: expose `start` function from loader
- e612f2a: Make compatible with Next.js 15
- be820c4: Bump deps
- Updated dependencies [e45bc67]
- Updated dependencies [d9e908e]
- Updated dependencies [d9e908e]
- Updated dependencies [f949520]
- Updated dependencies [9a0b09f]
- Updated dependencies [9a0b09f]
- Updated dependencies [367f4c3]
- Updated dependencies [e1ee822]
- Updated dependencies [e612f2a]
- Updated dependencies [9a0b09f]
- Updated dependencies [d9e908e]
- Updated dependencies [8ef00dc]
- Updated dependencies [979e301]
- Updated dependencies [d9e908e]
- Updated dependencies [979e301]
- Updated dependencies [15781f0]
- Updated dependencies [be820c4]
- Updated dependencies [d9e908e]
  - fumadocs-core@14.0.0

## 10.0.2

### Patch Changes

- f21c871: Change cache path of manifest files
- Updated dependencies [78e59e7]
  - fumadocs-core@13.4.8

## 10.0.1

### Patch Changes

- 7e23388: Fix windows compatibility
  - fumadocs-core@13.4.5

## 10.0.0

### Major Changes

- ed83d01: **Support declarative collections**

  **why:** This allows Fumadocs MDX to be more flexible.

  **migrate:**

  You don't need `exports` anymore, properties are merged into one object by default.

  ```diff
  - page.data.exports.toc
  + page.data.toc

  - page.data.exports.default
  + page.data.body
  ```

  A `source.config.ts` is now required.

  ```ts
  import { defineDocs, defineConfig } from 'fumadocs-mdx/config';

  export const { docs, meta } = defineDocs();

  export default defineConfig();
  ```

  The `mdx-components.tsx` file is no longer used, pass MDX components to body instead.

  Search indexes API is now replaced by Manifest API.

  Please refer to the docs for further details.

### Patch Changes

- 0c251e5: Bump deps
- Updated dependencies [7dabbc1]
- Updated dependencies [0c251e5]
- Updated dependencies [3b56170]
  - fumadocs-core@13.4.2

## 9.0.4

### Patch Changes

- 95dbba1: Support passing remark structure options
- Updated dependencies [95dbba1]
  - fumadocs-core@13.4.1

## 9.0.3

### Patch Changes

- c0d1faf: Store additional `_data` to search indexes
  - fumadocs-core@13.4.0

## 9.0.2

### Patch Changes

- 61b91fa: Improve Fumadocs OpenAPI support
- Updated dependencies [36b771b]
- Updated dependencies [61b91fa]
  - fumadocs-core@13.2.2

## 9.0.1

### Patch Changes

- c7aa090: Improve Fumadocs OpenAPI support
- Updated dependencies [17fa173]
  - fumadocs-core@13.2.1

## 9.0.0

### Major Changes

- 1f1989e: Support Fumadocs v13

### Patch Changes

- fumadocs-core@13.0.1

## 8.2.34

### Patch Changes

- c2d956b: Support mirror pages for symlinks of MDX file
  - fumadocs-core@12.5.3

## 8.2.33

### Patch Changes

- 78acd55: Use full mode on docs pages by default on OpenAPI generated pages
  - fumadocs-core@12.2.1

## 8.2.32

### Patch Changes

- 2eb68c8: Force a release of content sources
  - fumadocs-core@12.0.7

## 8.2.31

### Patch Changes

- 310e0ab: Move `fumadocs-core` to peer dependency
- Updated dependencies [053609d]
  - fumadocs-core@12.0.3

## 8.2.30

### Patch Changes

- fumadocs-core@12.0.2

## 8.2.29

### Patch Changes

- fumadocs-core@12.0.1

## 8.2.28

### Patch Changes

- Updated dependencies [98430e9]
- Updated dependencies [d88dfa6]
- Updated dependencies [ba20694]
- Updated dependencies [57eb762]
  - fumadocs-core@12.0.0

## 8.2.27

### Patch Changes

- Updated dependencies [1b8e12b]
  - fumadocs-core@11.3.2

## 8.2.26

### Patch Changes

- fumadocs-core@11.3.1

## 8.2.25

### Patch Changes

- 17e162e: Add `mdx` to page extensions by default
- Updated dependencies [917d87f]
  - fumadocs-core@11.3.0

## 8.2.24

### Patch Changes

- fumadocs-core@11.2.2

## 8.2.23

### Patch Changes

- fumadocs-core@11.2.1

## 8.2.22

### Patch Changes

- fumadocs-core@11.2.0

## 8.2.21

### Patch Changes

- 66a100d: Improve error messages
- Updated dependencies [88008b1]
- Updated dependencies [944541a]
- Updated dependencies [07a9312]
  - fumadocs-core@11.1.3

## 8.2.20

### Patch Changes

- fumadocs-core@11.1.2

## 8.2.19

### Patch Changes

- 8ef2b68: Bump deps
- Updated dependencies [8ef2b68]
- Updated dependencies [26f464d]
- Updated dependencies [26f464d]
  - fumadocs-core@11.1.1

## 8.2.18

### Patch Changes

- fumadocs-core@11.1.0

## 8.2.17

### Patch Changes

- Updated dependencies [98258b5]
  - fumadocs-core@11.0.8

## 8.2.16

### Patch Changes

- Updated dependencies [f7c2c5c]
  - fumadocs-core@11.0.7

## 8.2.15

### Patch Changes

- 5653d5d: Support customising heading id in headings
- 5653d5d: Support custom heading slugger
- Updated dependencies [5653d5d]
- Updated dependencies [5653d5d]
  - fumadocs-core@11.0.6

## 8.2.14

### Patch Changes

- fumadocs-core@11.0.5

## 8.2.13

### Patch Changes

- 7b61b2f: Migrate `fumadocs-ui` to fully ESM, adding support for ESM `tailwind.config` file
- Updated dependencies [7b61b2f]
  - fumadocs-core@11.0.4

## 8.2.12

### Patch Changes

- fumadocs-core@11.0.3

## 8.2.11

### Patch Changes

- fumadocs-core@11.0.2

## 8.2.10

### Patch Changes

- fumadocs-core@11.0.1

## 8.2.9

### Patch Changes

- Updated dependencies [2d8df75]
- Updated dependencies [92cb12f]
- Updated dependencies [f75287d]
- Updated dependencies [2d8df75]
  - fumadocs-core@11.0.0

## 8.2.8

### Patch Changes

- Updated dependencies [bbad52f]
  - fumadocs-core@10.1.3

## 8.2.7

### Patch Changes

- fumadocs-core@10.1.2

## 8.2.6

### Patch Changes

- Updated dependencies [779c599]
- Updated dependencies [0c01300]
- Updated dependencies [779c599]
  - fumadocs-core@10.1.1

## 8.2.5

### Patch Changes

- fumadocs-core@10.1.0

## 8.2.4

### Patch Changes

- e47c62f: Support customising included files in the map file
- Updated dependencies [e47c62f]
  - fumadocs-core@10.0.5

## 8.2.3

### Patch Changes

- fumadocs-core@10.0.4

## 8.2.2

### Patch Changes

- Updated dependencies [6f321e5]
  - fumadocs-core@10.0.3

## 8.2.1

### Patch Changes

- Updated dependencies [10e099a]
  - fumadocs-core@10.0.2

## 8.2.0

### Minor Changes

- 01155f5: Support generate search indexes in build time

### Patch Changes

- Updated dependencies [c9b7763]
- Updated dependencies [0e78dc8]
- Updated dependencies [d8483a8]
  - fumadocs-core@10.0.1

## 8.1.1

### Patch Changes

- Updated dependencies [b5d16938]
- Updated dependencies [321d1e1f]
  - fumadocs-core@10.0.0

## 8.1.0

### Minor Changes

- 1c388ca5: Support `defaultOpen` for folder nodes

### Patch Changes

- Updated dependencies [909b0e35]
- Updated dependencies [691f12aa]
- Updated dependencies [1c388ca5]
  - fumadocs-core@9.1.0

## 8.0.5

### Patch Changes

- fumadocs-core@9.0.0

## 8.0.4

### Patch Changes

- fumadocs-core@8.3.0

## 8.0.3

### Patch Changes

- 9bf5adb: Replace await imports with normal imports
- Updated dependencies [5c24659]
  - fumadocs-core@8.2.0

## 8.0.2

### Patch Changes

- fumadocs-core@8.1.1

## 8.0.1

### Patch Changes

- 6c5a39a: Rename Git repository to `fumadocs`
- Updated dependencies [6c5a39a]
- Updated dependencies [eb028b4]
- Updated dependencies [054ec60]
  - fumadocs-core@8.1.0

## 8.0.0

### Major Changes

- 1a346a1: **Enable `remark-image` plugin by default**

  You can add image embeds easily. They will be converted to static image imports.

  ```mdx
  ![banner](/image.png)
  ```

  Become:

  ```mdx
  import img_banner from '../../public/image.png';

  <img alt="banner" src={img_banner} />
  ```

- 2b11c20: **Rename to Fumadocs**

  `next-docs-zeta` -> `fumadocs-core`

  `next-docs-ui` -> `fumadocs-ui`

  `next-docs-mdx` -> `fumadocs-mdx`

  `@fuma-docs/openapi` -> `fumadocs-openapi`

  `create-next-docs-app` -> `create-fumadocs-app`

### Patch Changes

- Updated dependencies [2ea9437]
- Updated dependencies [cdff313]
- Updated dependencies [1a346a1]
- Updated dependencies [2b11c20]
  - fumadocs-core@8.0.0

## 7.1.2

### Patch Changes

- next-docs-zeta@7.1.2

## 7.1.1

### Patch Changes

- next-docs-zeta@7.1.1

## 7.1.0

### Patch Changes

- next-docs-zeta@7.1.0

## 7.0.0

### Major Changes

- 9929c5b: **Prefer `.map.ts` instead of `_map.ts`**

  Unless you have especially configured, now it uses `.map.ts` by default.

  ```diff
  - import map from "@/_map"
  + import map from "@/.map"
  ```

- 9929c5b: **Migrate to Source API**

  `fromMap` has been removed. Please use `createMDXSource` instead.

  ```ts
  import { map } from '@/.map';
  import { createMDXSource } from 'next-docs-mdx';
  import { loader } from 'next-docs-zeta/source';

  export const { getPage, getPages, pageTree } = loader({
    baseUrl: '/docs',
    rootDir: 'docs',
    source: createMDXSource(map),
  });
  ```

### Minor Changes

- 8fd769f: **Support last modified timestamp for Git**

  Enable this in `next.config.mjs`:

  ```js
  const withNextDocs = createNextDocs({
    mdxOptions: {
      lastModifiedTime: 'git',
    },
  });
  ```

  Access it via `page.data.exports.lastModified`.

### Patch Changes

- Updated dependencies [9929c5b]
- Updated dependencies [9929c5b]
- Updated dependencies [49201be]
- Updated dependencies [338ea98]
- Updated dependencies [4c1334e]
- Updated dependencies [9929c5b]
  - next-docs-zeta@7.0.0

## 6.1.0

### Patch Changes

- Updated dependencies [f39ae40]
  - next-docs-zeta@6.1.0

## 6.0.2

### Patch Changes

- 1845bf5: Fixes import path for next-docs-mdx/loader-mdx
  - next-docs-zeta@6.0.2

## 6.0.1

### Patch Changes

- next-docs-zeta@6.0.1

## 6.0.0

### Major Changes

- 69f8abf: **Make file paths relative to `rootDir` when resolving files**

  For a more simplified usage, the resolved file paths will be relative to `rootDir`.

  You can now generate slugs automatically depending on the root directory you have configured.

  ```ts
  const utils = fromMap(map, {
    rootDir: 'ui',
    schema: {
      frontmatter: frontmatterSchema,
    },
  });
  ```

  The configuration above will generate `/hello` slugs for a file named `/content/ui/hello.mdx`, while the previous one generates `/ui/hello`.

- 9ef047d: **Pre-bundle page urls into raw pages.**

  This means you don't need `getPageUrl` anymore for built-in adapters, including `next-docs-mdx` and Contentlayer. It is now replaced by the `url` property from the pages array provided by your adapter.

  Due to this change, your old configuration might not continues to work.

  ```diff
  import { fromMap } from 'next-docs-mdx/map'

  fromMap({
  -  slugs: ...
  +  getSlugs: ...
  })
  ```

  For Contentlayer, the `getUrl` option is now moved to `createConfig`.

- 1c187b9: **Support intelligent schema types**

  The `validate` options is now renamed to `schema`.

  ```ts
  import { defaultSchemas, fromMap } from 'next-docs-mdx/map';

  const utils = fromMap(map, {
    rootDir: 'docs/ui',
    baseUrl: '/docs/ui',
    schema: {
      frontmatter: defaultSchemas.frontmatter.extend({
        preview: z.string().optional(),
      }),
    },
  });
  ```

  The `frontmatter` field on pages should be automatically inferred to your Zod schema type.

- 52b24a6: **Remove `/docs` from default root content path**

  Previously, the default root content path is `./content/docs`. All your documents must be placed under the root directory.

  Since this update, it is now `./content` by default. To keep the old behaviours, you may manually specify `rootContentPath`.

  ```js
  const withNextDocs = createNextDocs({
    rootContentPath: './content/docs',
  });
  ```

  **Notice that due to this change, your `baseUrl` property will be `/` by default**

  ```diff
  const withNextDocs = createNextDocs({
  +  baseUrl: "/docs"
  })
  ```

- 2ff7581: **Rename configuration options**

  The options of `createNextDocs` is now renamed to be more flexible and straightforward.

  | Old             | New                                |
  | --------------- | ---------------------------------- |
  | `dataExports`   | `mdxOptions.valueToExport`         |
  | `pluginOptions` | `mdxOptions.rehypeNextDocsOptions` |

  `rehypePlugins` and `remarkPlugins` can also be a function that accepts and returns plugins.

### Minor Changes

- 55a2321: **Use `@mdx-js/mdx` to process MDX/markdown files.**

  You no longer need `@next/loader` and `@mdx-js/loader` to be installed on your project, `next-docs-mdx` will process files with `@mdx-js/mdx` directly.

  _This change will not break most of the projects_

### Patch Changes

- Updated dependencies [9ef047d]
  - next-docs-zeta@6.0.0

## 5.0.0

### Minor Changes

- de44efe: Migrate to Shikiji
- de44efe: Support code highlighting options

### Patch Changes

- Updated dependencies [de44efe]
- Updated dependencies [de44efe]
  - next-docs-zeta@5.0.0

## 4.0.9

### Patch Changes

- Updated dependencies [a883009]
  - next-docs-zeta@4.0.9

## 4.0.8

### Patch Changes

- Updated dependencies [e0c5c96]
  - next-docs-zeta@4.0.8

## 4.0.7

### Patch Changes

- b9af5ed: Update tsup & dependencies
- Updated dependencies [b9af5ed]
  - next-docs-zeta@4.0.7

## 4.0.6

### Patch Changes

- Updated dependencies [ff38f6e]
  - next-docs-zeta@4.0.6

## 4.0.5

### Patch Changes

- next-docs-zeta@4.0.5

## 4.0.4

### Patch Changes

- next-docs-zeta@4.0.4

## 4.0.3

### Patch Changes

- ba51a9f: Support custom slugs function
- 0cc10cb: Support custom build page tree options
- Updated dependencies [0cc10cb]
  - next-docs-zeta@4.0.3

## 4.0.2

### Patch Changes

- 347df32: Fix empty `baseUrl` unexpected behaviours
- ad7b8a8: Fully support custom root content directory paths
- 73f985a: Support `rootDir` API
  - next-docs-zeta@4.0.2

## 4.0.1

### Patch Changes

- 01b23e2: Support Next.js 14
- Updated dependencies [2da93d8]
- Updated dependencies [01b23e2]
  - next-docs-zeta@4.0.1

## 4.0.0

### Patch Changes

- Updated dependencies [6c4a782]
- Updated dependencies [6c4a782]
  - next-docs-zeta@4.0.0

## 4.0.0

### Patch Changes

- Updated dependencies [678cd3d]
- Updated dependencies [24245a3]
  - next-docs-zeta@4.0.0

## 3.0.0

### Patch Changes

- Updated dependencies [1043532]
- Updated dependencies [7a0690b]
- Updated dependencies [a4a8120]
  - next-docs-zeta@3.0.0
`````

## File: packages/mdx-remote/test/fixtures/file.mdx
`````
## You **found** `me`!
`````

## File: packages/mdx-remote/test/fixtures/index.mdx
`````
---
title: Hello World
description: Something
---

Hey!

```tsx
console.log('Hello World');
```

| Name | Description |
| ---- | ----------- |
| Fuma | Love anime  |
`````

## File: packages/mdx-remote/CHANGELOG.md
`````markdown
# @fumadocs/mdx-remote

## 1.4.0

### Minor Changes

- f8a58c6: Support `preset: minimal` to disable Fumadocs specific defaults

### Patch Changes

- Updated dependencies [658fa96]
  - fumadocs-core@15.6.5

## 1.3.4

### Patch Changes

- d0f8a15: Enable `remarkNpm` by default, replace `remarkInstall` with it.
- Updated dependencies [d0f8a15]
- Updated dependencies [84918b8]
- Updated dependencies [f8d1709]
  - fumadocs-core@15.6.0

## 1.3.3

### Patch Changes

- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos
- Updated dependencies [7a45921]
- Updated dependencies [1b7bc4b]
  - fumadocs-core@15.5.2

## 1.3.2

### Patch Changes

- a6c909b: Removed unused devDependencies and migrated from `fast-glob` to `tinyglobby`
  - fumadocs-core@15.3.4

## 1.3.1

### Patch Changes

- 4ae7b4a: Support MDX in codeblock tab value
- Updated dependencies [4ae7b4a]
  - fumadocs-core@15.3.3

## 1.3.0

### Minor Changes

- 363055d: Support `/client` API for browser usage
- cf87f9d: Support `compiler.compileFile`, deprecate `skipRender` option in favour of this
- cf87f9d: Deprecate `executeMdx` in favour of `compiler.render`

### Patch Changes

- Updated dependencies [2fd325c]
- Updated dependencies [a7cf4fa]
  - fumadocs-core@15.2.0

## 1.2.1

### Patch Changes

- 6493817: Load plugins conditionally for current Fumadocs version
- Updated dependencies [c5add28]
- Updated dependencies [f3cde4f]
- Updated dependencies [7c8a690]
- Updated dependencies [b812457]
  - fumadocs-core@15.1.1

## 1.2.0

### Minor Changes

- 69f20cb: Remove `content` property from the output of `compile`

### Patch Changes

- fumadocs-core@15.0.3

## 1.1.3

### Patch Changes

- a89d6e0: Support Fumadocs v15
- Updated dependencies [5b8cca8]
- Updated dependencies [a763058]
- Updated dependencies [581f4a5]
  - fumadocs-core@15.0.0

## 1.1.2

### Patch Changes

- 3bde5cc: Support JSX nodes in TOC
  - fumadocs-core@14.7.7

## 1.1.1

### Patch Changes

- b9601fb: Update Shiki
- 1142b8c: Support `createCompiler` API
- Updated dependencies [b9601fb]
  - fumadocs-core@14.7.6

## 1.1.0

### Minor Changes

- f2e880f: Deprecate `content`, prefer `body` instead

### Patch Changes

- f2e880f: Support more options for `compile()`
- Updated dependencies [777188b]
  - fumadocs-core@14.7.5

## 1.0.0

### Major Changes

- 82ff9ec: **Remove GitHub remote integration**

  **why:** It should be equivalent to `next-mdx-remote` but include extra functionalities by Fumadocs, like built-in MDX plugins, table of contents and frontmatter parsing.

  **migrate:** Implement your own content source, or see our Sanity/BaseHub examples for CMS usages.

## 0.2.4

### Patch Changes

- 4766292: Support React 19
- Updated dependencies [4dfde6b]
- Updated dependencies [bebb16b]
- Updated dependencies [4766292]
- Updated dependencies [050b326]
  - fumadocs-core@14.6.0

## 0.2.3

### Patch Changes

- e612f2a: Make compatible with Next.js 15
- be820c4: Bump deps
- Updated dependencies [e45bc67]
- Updated dependencies [d9e908e]
- Updated dependencies [d9e908e]
- Updated dependencies [f949520]
- Updated dependencies [9a0b09f]
- Updated dependencies [9a0b09f]
- Updated dependencies [367f4c3]
- Updated dependencies [e1ee822]
- Updated dependencies [e612f2a]
- Updated dependencies [9a0b09f]
- Updated dependencies [d9e908e]
- Updated dependencies [8ef00dc]
- Updated dependencies [979e301]
- Updated dependencies [d9e908e]
- Updated dependencies [979e301]
- Updated dependencies [15781f0]
- Updated dependencies [be820c4]
- Updated dependencies [d9e908e]
  - fumadocs-core@14.0.0

## 0.2.2

### Patch Changes

- 0c251e5: Bump deps
- Updated dependencies [7dabbc1]
- Updated dependencies [0c251e5]
- Updated dependencies [3b56170]
  - fumadocs-core@13.4.2

## 0.2.1

### Patch Changes

- 758013f: Use Fumadocs Remark Image instead of `rehype-img-size`
- Updated dependencies [36b771b]
- Updated dependencies [61b91fa]
  - fumadocs-core@13.2.2

## 0.2.0

### Minor Changes

- e6e1d9f: Improve Hot Reload

### Patch Changes

- fumadocs-core@12.4.1

## 0.1.0

### Minor Changes

- ca7d0f4: Support built-in search index build utility

### Patch Changes

- Updated dependencies [ca7d0f4]
  - fumadocs-core@12.3.2

## 0.0.2

### Patch Changes

- a39dbcb: Support Github Integration
- Updated dependencies [a39dbcb]
  - fumadocs-core@12.1.1

## 0.0.1

### Patch Changes

- e7f4edf: Support remote MDX files with `@fumadocs/remote-mdx`
  - fumadocs-core@12.0.7
`````

## File: packages/openapi/test/out/museum/events.mdx
`````
---
title: Events
description: Special events hosted by the Museum
full: true
_openapi:
  toc:
    - depth: 2
      title: List special events
      url: '#list-special-events'
    - depth: 2
      title: Create special events
      url: '#create-special-events'
    - depth: 2
      title: Get special event
      url: '#get-special-event'
    - depth: 2
      title: Update special event
      url: '#update-special-event'
    - depth: 2
      title: Delete special event
      url: '#delete-special-event'
  structuredData:
    headings:
      - content: List special events
        id: list-special-events
      - content: Create special events
        id: create-special-events
      - content: Get special event
        id: get-special-event
      - content: Update special event
        id: update-special-event
      - content: Delete special event
        id: delete-special-event
    contents:
      - content: Return a list of upcoming special events at the museum.
        heading: list-special-events
      - content: Creates a new special event for the museum.
        heading: create-special-events
      - content: Get details about a special event.
        heading: get-special-event
      - content: Update the details of a special event
        heading: update-special-event
      - content: >-
          Delete a special event from the collection. Allows museum to cancel
          planned events.
        heading: delete-special-event
---

{/* This file was generated by Fumadocs. Do not edit this file directly. Any changes should be made by running the generation command again. */}

<APIPage document={"./fixtures/museum.yaml"} operations={[{"path":"/special-events","method":"get"},{"path":"/special-events","method":"post"},{"path":"/special-events/{eventId}","method":"get"},{"path":"/special-events/{eventId}","method":"patch"},{"path":"/special-events/{eventId}","method":"delete"}]} webhooks={[]} hasHead={true} />
`````

## File: packages/openapi/test/out/museum/operations.mdx
`````
---
title: Operations
description: Operational information about the museum.
full: true
_openapi:
  method: GET
  route: /museum-hours
  toc:
    - depth: 2
      title: Get museum hours
      url: '#get-museum-hours'
  structuredData:
    headings:
      - content: Get museum hours
        id: get-museum-hours
    contents:
      - content: Get upcoming museum operating hours
        heading: get-museum-hours
---

{/* This file was generated by Fumadocs. Do not edit this file directly. Any changes should be made by running the generation command again. */}

<APIPage document={"./fixtures/museum.yaml"} operations={[{"path":"/museum-hours","method":"get"}]} webhooks={[]} hasHead={true} />
`````

## File: packages/openapi/test/out/museum/tickets.mdx
`````
---
title: Tickets
description: Museum tickets for general entrance or special events.
full: true
_openapi:
  toc:
    - depth: 2
      title: Buy museum tickets
      url: '#buy-museum-tickets'
    - depth: 2
      title: Get ticket QR code
      url: '#get-ticket-qr-code'
  structuredData:
    headings:
      - content: Buy museum tickets
        id: buy-museum-tickets
      - content: Get ticket QR code
        id: get-ticket-qr-code
    contents:
      - content: Purchase museum tickets for general entry or special events.
        heading: buy-museum-tickets
      - content: >-
          Return an image of your ticket with scannable QR code. Used for event
          entry.
        heading: get-ticket-qr-code
---

{/* This file was generated by Fumadocs. Do not edit this file directly. Any changes should be made by running the generation command again. */}

<APIPage document={"./fixtures/museum.yaml"} operations={[{"path":"/tickets","method":"post"},{"path":"/tickets/{ticketId}/qr","method":"get"}]} webhooks={[]} hasHead={true} />
`````

## File: packages/openapi/test/out/unkey/apis.mdx
`````
---
title: Apis
full: true
_openapi:
  toc:
    - depth: 2
      title: Get Api
      url: '#get-api'
    - depth: 2
      title: Create Api
      url: '#create-api'
    - depth: 2
      title: List Keys
      url: '#list-keys'
    - depth: 2
      title: Delete Api
      url: '#delete-api'
  structuredData:
    headings:
      - content: Get Api
        id: get-api
      - content: Create Api
        id: create-api
      - content: List Keys
        id: list-keys
      - content: Delete Api
        id: delete-api
    contents: []
---

<APIPage document={"./fixtures/unkey.json"} operations={[{"method":"get","path":"/v1/apis.getApi"},{"method":"post","path":"/v1/apis.createApi"},{"method":"get","path":"/v1/apis.listKeys"},{"method":"post","path":"/v1/apis.deleteApi"}]} hasHead={true} />
`````

## File: packages/openapi/test/out/unkey/keys.mdx
`````
---
title: Keys
full: true
_openapi:
  toc:
    - depth: 2
      title: Get Key
      url: '#get-key'
    - depth: 2
      title: Delete Key
      url: '#delete-key'
    - depth: 2
      title: Create Key
      url: '#create-key'
    - depth: 2
      title: Verify Key
      url: '#verify-key'
    - depth: 2
      title: Update Key
      url: '#update-key'
    - depth: 2
      title: Update Remaining
      url: '#update-remaining'
    - depth: 2
      title: Get Verifications
      url: '#get-verifications'
  structuredData:
    headings:
      - content: Get Key
        id: get-key
      - content: Delete Key
        id: delete-key
      - content: Create Key
        id: create-key
      - content: Verify Key
        id: verify-key
      - content: Update Key
        id: update-key
      - content: Update Remaining
        id: update-remaining
      - content: Get Verifications
        id: get-verifications
    contents: []
---

<APIPage document={"./fixtures/unkey.json"} operations={[{"method":"get","path":"/v1/keys.getKey"},{"method":"post","path":"/v1/keys.deleteKey"},{"method":"post","path":"/v1/keys.createKey"},{"method":"post","path":"/v1/keys.verifyKey"},{"method":"post","path":"/v1/keys.updateKey"},{"method":"post","path":"/v1/keys.updateRemaining"},{"method":"get","path":"/v1/keys.getVerifications"}]} hasHead={true} />
`````

## File: packages/openapi/test/out/unkey/liveness.mdx
`````
---
title: Liveness
full: true
_openapi:
  toc:
    - depth: 2
      title: Check Liveness
      url: '#check-liveness'
  structuredData:
    headings:
      - content: Check Liveness
        id: check-liveness
    contents: []
---

<APIPage document={"./fixtures/unkey.json"} operations={[{"method":"get","path":"/v1/liveness"}]} hasHead={true} />
`````

## File: packages/openapi/test/out/unkey/migrations.mdx
`````
---
title: migrations
full: true
---

import { Root, API, APIInfo, APIExample, Responses, Response, ResponseTypes, ExampleResponse, TypeScriptResponse, Property, ObjectCollapsible, Requests, Request, APIPlayground } from "fumadocs-ui/components/api";

<Root baseUrl={"https://api.unkey.dev"}>

<API>

<APIInfo method={"POST"} route={"/v1/migrations.createKeys"}>

## v1.migrations.createKeys

### Authorization

<Property name={"Authorization"} type={"Bearer <token>"} required={true}>

In: `header`

</Property>

### Request Body

<Property name={"body"} type={"array<object>"} required={true} deprecated={undefined}>

<ObjectCollapsible name={"Object 1"}>

<Property name={"apiId"} type={"string"} required={true} deprecated={undefined}>

Choose an `API` where this key should be created.

<span>Example: `"api_123"`</span>

</Property>

<Property name={"prefix"} type={"string"} required={false} deprecated={undefined}>

To make it easier for your users to understand which product an api key belongs to, you can add prefix them.

For example Stripe famously prefixes their customer ids with cus_ or their api keys with sk_live_.

The underscore is automatically added if you are defining a prefix, for example: "prefix": "abc" will result in a key like abc_xxxxxxxxx


<span>Maximum length: `8`</span>

</Property>

<Property name={"name"} type={"string"} required={false} deprecated={undefined}>

The name for your Key. This is not customer facing.

<span>Example: `"my key"`</span>

</Property>

<Property name={"plaintext"} type={"string"} required={false} deprecated={undefined}>

The raw key in plaintext. If provided, unkey encrypts this value and stores it securely. Provide either `hash` or `plaintext`

</Property>

<Property name={"hash"} type={"object"} required={false} deprecated={undefined}>

Provide either `hash` or `plaintext`

<ObjectCollapsible name={"hash"}>

<Property name={"value"} type={"string"} required={true} deprecated={undefined}>

The hashed and encoded key

</Property>

<Property name={"variant"} type={"string"} required={true} deprecated={undefined}>

The algorithm for hashing and encoding, currently only sha256 and base64 are supported

<span>Value in: `"sha256_base64"`</span>

</Property>

</ObjectCollapsible>

</Property>

<Property name={"start"} type={"string"} required={false} deprecated={undefined}>

The first 4 characters of the key. If a prefix is used, it should be the prefix plus 4 characters.

<span>Example: `"unkey_32kq"`</span>

</Property>

<Property name={"ownerId"} type={"string"} required={false} deprecated={undefined}>

Your user’s Id. This will provide a link between Unkey and your customer record.
When validating a key, we will return this back to you, so you can clearly identify your user from their api key.

<span>Example: `"team_123"`</span>

</Property>

<Property name={"meta"} type={"object"} required={false} deprecated={undefined}>

This is a place for dynamic meta data, anything that feels useful for you should go here

<span>Example: `{"billingTier":"PRO","trialEnds":"2023-06-16T17:16:37.161Z"}`</span>

<ObjectCollapsible name={"meta"}>

<Property name={"[key: string]"} type={"null"} required={false} deprecated={undefined}>

</Property>

</ObjectCollapsible>

</Property>

<Property name={"roles"} type={"array<string>"} required={false} deprecated={undefined}>

A list of roles that this key should have. If the role does not exist, an error is thrown

<span>Example: `["admin","finance"]`</span>

</Property>

<Property name={"permissions"} type={"array<string>"} required={false} deprecated={undefined}>

A list of permissions that this key should have. If the permission does not exist, an error is thrown

<span>Example: `["domains.create_record","say_hello"]`</span>

</Property>

<Property name={"expires"} type={"integer"} required={false} deprecated={undefined}>

You can auto expire keys by providing a unix timestamp in milliseconds. Once Keys expire they will automatically be disabled and are no longer valid unless you enable them again.

<span>Example: `1623869797161`</span>

</Property>

<Property name={"remaining"} type={"integer"} required={false} deprecated={undefined}>

You can limit the number of requests a key can make. Once a key reaches 0 remaining requests, it will automatically be disabled and is no longer valid unless you update it.

<span>Example: `1000`</span>

<span>Minimum: `1`</span>

</Property>

<Property name={"refill"} type={"object"} required={false} deprecated={undefined}>

Unkey enables you to refill verifications for each key at regular intervals.

<span>Example: `{"interval":"daily","amount":100}`</span>

<ObjectCollapsible name={"refill"}>

<Property name={"interval"} type={"string"} required={true} deprecated={undefined}>

Unkey will automatically refill verifications at the set interval.

<span>Value in: `"daily" | "monthly"`</span>

</Property>

<Property name={"amount"} type={"integer"} required={true} deprecated={undefined}>

The number of verifications to refill for each occurrence is determined individually for each key.

<span>Minimum: `0`</span>

</Property>

</ObjectCollapsible>

</Property>

<Property name={"ratelimit"} type={"object"} required={false} deprecated={undefined}>

Unkey comes with per-key ratelimiting out of the box.

<span>Example: `{"type":"fast","limit":10,"refillRate":1,"refillInterval":60}`</span>

<ObjectCollapsible name={"ratelimit"}>

<Property name={"async"} type={"boolean"} required={false} deprecated={undefined}>

Async will return a response immediately, lowering latency at the cost of accuracy.

<span>Default: `false`</span>

</Property>

<Property name={"type"} type={"string"} required={false} deprecated={true}>

Fast ratelimiting doesn't add latency, while consistent ratelimiting is more accurate.

<span>Default: `"fast"`</span>

<span>Value in: `"fast" | "consistent"`</span>

</Property>

<Property name={"limit"} type={"integer"} required={true} deprecated={undefined}>

The total amount of burstable requests.

<span>Minimum: `1`</span>

</Property>

<Property name={"refillRate"} type={"integer"} required={true} deprecated={true}>

How many tokens to refill during each refillInterval.

<span>Minimum: `1`</span>

</Property>

<Property name={"refillInterval"} type={"integer"} required={true} deprecated={true}>

Determines the speed at which tokens are refilled, in milliseconds.

<span>Minimum: `1`</span>

</Property>

</ObjectCollapsible>

</Property>

<Property name={"enabled"} type={"boolean"} required={false} deprecated={undefined}>

Sets if key is enabled or disabled. Disabled keys are not valid.

<span>Example: `false`</span>

<span>Default: `true`</span>

</Property>

<Property name={"environment"} type={"string"} required={false} deprecated={undefined}>

Environments allow you to divide your keyspace.

Some applications like Stripe, Clerk, WorkOS and others have a concept of "live" and "test" keys to
give the developer a way to develop their own application without the risk of modifying real world
resources.

When you set an environment, we will return it back to you when validating the key, so you can
handle it correctly.
              

<span>Maximum length: `256`</span>

</Property>

</ObjectCollapsible>

</Property>

| Status code | Description |
| ----------- | ----------- |
| `200` | The key ids of all created keys |
| `400` | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |
| `401` | Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response. |
| `403` | The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server. |
| `404` | The server cannot find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web. |
| `409` | This response is sent when a request conflicts with the current state of the server. |
| `429` | The user has sent too many requests in a given amount of time ("rate limiting") |
| `500` | The server has encountered a situation it does not know how to handle. |

<APIPlayground authorization={{"type":"string","name":"authorization","defaultValue":"Bearer","isRequired":true,"description":"The authorization token"}} method={"POST"} route={"/v1/migrations.createKeys"} path={[]} query={[]} header={[]} body={{"type":"array","isRequired":true,"items":"0"}} schemas={{"0":{"type":"object","isRequired":false,"properties":{"apiId":{"type":"ref","isRequired":true,"schema":"1"},"prefix":{"type":"ref","isRequired":false,"schema":"2"},"name":{"type":"ref","isRequired":false,"schema":"3"},"plaintext":{"type":"ref","isRequired":false,"schema":"4"},"hash":{"type":"ref","isRequired":false,"schema":"5"},"start":{"type":"ref","isRequired":false,"schema":"8"},"ownerId":{"type":"ref","isRequired":false,"schema":"9"},"meta":{"type":"ref","isRequired":false,"schema":"10"},"roles":{"type":"ref","isRequired":false,"schema":"11"},"permissions":{"type":"ref","isRequired":false,"schema":"13"},"expires":{"type":"ref","isRequired":false,"schema":"15"},"remaining":{"type":"ref","isRequired":false,"schema":"16"},"refill":{"type":"ref","isRequired":false,"schema":"17"},"ratelimit":{"type":"ref","isRequired":false,"schema":"20"},"enabled":{"type":"ref","isRequired":false,"schema":"26"},"environment":{"type":"ref","isRequired":false,"schema":"27"}}},"1":{"type":"string","defaultValue":"api_123","isRequired":false,"description":"Choose an `API` where this key should be created."},"2":{"type":"string","defaultValue":"","isRequired":false,"description":"To make it easier for your users to understand which product an api key belongs to, you can add prefix them.\n\nFor example Stripe famously prefixes their customer ids with cus_ or their api keys with sk_live_.\n\nThe underscore is automatically added if you are defining a prefix, for example: \"prefix\": \"abc\" will result in a key like abc_xxxxxxxxx\n"},"3":{"type":"string","defaultValue":"my key","isRequired":false,"description":"The name for your Key. This is not customer facing."},"4":{"type":"string","defaultValue":"","isRequired":false,"description":"The raw key in plaintext. If provided, unkey encrypts this value and stores it securely. Provide either `hash` or `plaintext`"},"5":{"type":"object","isRequired":false,"description":"Provide either `hash` or `plaintext`","properties":{"value":{"type":"ref","isRequired":true,"schema":"6"},"variant":{"type":"ref","isRequired":true,"schema":"7"}}},"6":{"type":"string","defaultValue":"","isRequired":false,"description":"The hashed and encoded key"},"7":{"type":"string","defaultValue":"","isRequired":false,"description":"The algorithm for hashing and encoding, currently only sha256 and base64 are supported"},"8":{"type":"string","defaultValue":"unkey_32kq","isRequired":false,"description":"The first 4 characters of the key. If a prefix is used, it should be the prefix plus 4 characters."},"9":{"type":"string","defaultValue":"team_123","isRequired":false,"description":"Your user’s Id. This will provide a link between Unkey and your customer record.\nWhen validating a key, we will return this back to you, so you can clearly identify your user from their api key."},"10":{"type":"object","isRequired":false,"description":"This is a place for dynamic meta data, anything that feels useful for you should go here","properties":{}},"11":{"type":"array","description":"A list of roles that this key should have. If the role does not exist, an error is thrown","isRequired":false,"items":"12"},"12":{"type":"string","defaultValue":"","isRequired":false},"13":{"type":"array","description":"A list of permissions that this key should have. If the permission does not exist, an error is thrown","isRequired":false,"items":"14"},"14":{"type":"string","defaultValue":"","isRequired":false},"15":{"type":"number","defaultValue":1623869797161,"isRequired":false,"description":"You can auto expire keys by providing a unix timestamp in milliseconds. Once Keys expire they will automatically be disabled and are no longer valid unless you enable them again."},"16":{"type":"number","defaultValue":1000,"isRequired":false,"description":"You can limit the number of requests a key can make. Once a key reaches 0 remaining requests, it will automatically be disabled and is no longer valid unless you update it."},"17":{"type":"object","isRequired":false,"description":"Unkey enables you to refill verifications for each key at regular intervals.","properties":{"interval":{"type":"ref","isRequired":true,"schema":"18"},"amount":{"type":"ref","isRequired":true,"schema":"19"}}},"18":{"type":"string","defaultValue":"","isRequired":false,"description":"Unkey will automatically refill verifications at the set interval."},"19":{"type":"number","defaultValue":"","isRequired":false,"description":"The number of verifications to refill for each occurrence is determined individually for each key."},"20":{"type":"object","isRequired":false,"description":"Unkey comes with per-key ratelimiting out of the box.","properties":{"async":{"type":"ref","isRequired":false,"schema":"21"},"type":{"type":"ref","isRequired":false,"schema":"22"},"limit":{"type":"ref","isRequired":true,"schema":"23"},"refillRate":{"type":"ref","isRequired":true,"schema":"24"},"refillInterval":{"type":"ref","isRequired":true,"schema":"25"}}},"21":{"type":"boolean","defaultValue":"","isRequired":false,"description":"Async will return a response immediately, lowering latency at the cost of accuracy."},"22":{"type":"string","defaultValue":"","isRequired":false,"description":"Fast ratelimiting doesn't add latency, while consistent ratelimiting is more accurate."},"23":{"type":"number","defaultValue":"","isRequired":false,"description":"The total amount of burstable requests."},"24":{"type":"number","defaultValue":"","isRequired":false,"description":"How many tokens to refill during each refillInterval."},"25":{"type":"number","defaultValue":"","isRequired":false,"description":"Determines the speed at which tokens are refilled, in milliseconds."},"26":{"type":"boolean","defaultValue":false,"isRequired":false,"description":"Sets if key is enabled or disabled. Disabled keys are not valid."},"27":{"type":"string","defaultValue":"","isRequired":false,"description":"Environments allow you to divide your keyspace.\n\nSome applications like Stripe, Clerk, WorkOS and others have a concept of \"live\" and \"test\" keys to\ngive the developer a way to develop their own application without the risk of modifying real world\nresources.\n\nWhen you set an environment, we will return it back to you when validating the key, so you can\nhandle it correctly.\n              "}}}>

</APIPlayground>

</APIInfo>

<APIExample>

<Requests items={["cURL","JavaScript"]}>

<Request value={"cURL"}>

```bash
curl -X POST "https://api.unkey.dev/v1/migrations.createKeys" \
  -d '[
  {
    "apiId": "api_123",
    "prefix": "string",
    "name": "my key",
    "plaintext": "string",
    "hash": {
      "value": "string",
      "variant": "sha256_base64"
    },
    "start": "unkey_32kq",
    "ownerId": "team_123",
    "meta": {
      "billingTier": "PRO",
      "trialEnds": "2023-06-16T17:16:37.161Z"
    },
    "roles": [
      "admin",
      "finance"
    ],
    "permissions": [
      "domains.create_record",
      "say_hello"
    ],
    "expires": 1623869797161,
    "remaining": 1000,
    "refill": {
      "interval": "daily",
      "amount": 100
    },
    "ratelimit": {
      "type": "fast",
      "limit": 10,
      "refillRate": 1,
      "refillInterval": 60
    },
    "enabled": false,
    "environment": "string"
  }
]'
```

</Request>

<Request value={"JavaScript"}>

```js
fetch("https://api.unkey.dev/v1/migrations.createKeys", {
  method: "POST"
});
```

</Request>

</Requests>

<Responses items={["200","400","401","403","404","409","429","500"]}>

<Response value={"200"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "keyIds": [
    "key_123",
    "key_456"
  ]
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  /**
   * The ids of the keys. This is not a secret and can be stored as a reference if you wish. You need the keyId to update or delete a key later.
   */
  keyIds: string[];
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"400"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "BAD_REQUEST",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/BAD_REQUEST",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "BAD_REQUEST";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"401"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/UNAUTHORIZED",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "UNAUTHORIZED";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"403"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "FORBIDDEN",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/FORBIDDEN",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "FORBIDDEN";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"404"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "NOT_FOUND",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/NOT_FOUND",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "NOT_FOUND";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"409"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "CONFLICT",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/CONFLICT",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "CONFLICT";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"429"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "TOO_MANY_REQUESTS",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/TOO_MANY_REQUESTS",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "TOO_MANY_REQUESTS";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"500"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "INTERNAL_SERVER_ERROR",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/INTERNAL_SERVER_ERROR",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "INTERNAL_SERVER_ERROR";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

</Responses>

</APIExample>

</API>

<API>

<APIInfo method={"POST"} route={"/v1/migrations.enqueueKeys"}>

## v1.migrations.enqueueKeys

### Authorization

<Property name={"Authorization"} type={"Bearer <token>"} required={true}>

In: `header`

</Property>

### Request Body

<Property name={"migrationId"} type={"string"} required={true} deprecated={undefined}>

Contact support@unkey.dev to receive your migration id.

</Property>

<Property name={"apiId"} type={"string"} required={true} deprecated={undefined}>

The id of the api, you want to migrate keys to

</Property>

<Property name={"keys"} type={"array<object>"} required={true} deprecated={undefined}>

<ObjectCollapsible name={"Object 1"}>

<Property name={"prefix"} type={"string"} required={false} deprecated={undefined}>

To make it easier for your users to understand which product an api key belongs to, you can add prefix them.

For example Stripe famously prefixes their customer ids with cus_ or their api keys with sk_live_.

The underscore is automatically added if you are defining a prefix, for example: "prefix": "abc" will result in a key like abc_xxxxxxxxx


<span>Maximum length: `8`</span>

</Property>

<Property name={"name"} type={"string"} required={false} deprecated={undefined}>

The name for your Key. This is not customer facing.

<span>Example: `"my key"`</span>

</Property>

<Property name={"plaintext"} type={"string"} required={false} deprecated={undefined}>

The raw key in plaintext. If provided, unkey encrypts this value and stores it securely. Provide either `hash` or `plaintext`

</Property>

<Property name={"hash"} type={"object"} required={false} deprecated={undefined}>

Provide either `hash` or `plaintext`

<ObjectCollapsible name={"hash"}>

<Property name={"value"} type={"string"} required={true} deprecated={undefined}>

The hashed and encoded key

</Property>

<Property name={"variant"} type={"string"} required={true} deprecated={undefined}>

The algorithm for hashing and encoding, currently only sha256 and base64 are supported

<span>Value in: `"sha256_base64"`</span>

</Property>

</ObjectCollapsible>

</Property>

<Property name={"start"} type={"string"} required={false} deprecated={undefined}>

The first 4 characters of the key. If a prefix is used, it should be the prefix plus 4 characters.

<span>Example: `"unkey_32kq"`</span>

</Property>

<Property name={"ownerId"} type={"string"} required={false} deprecated={undefined}>

Your user’s Id. This will provide a link between Unkey and your customer record.
When validating a key, we will return this back to you, so you can clearly identify your user from their api key.

<span>Example: `"team_123"`</span>

</Property>

<Property name={"meta"} type={"object"} required={false} deprecated={undefined}>

This is a place for dynamic meta data, anything that feels useful for you should go here

<span>Example: `{"billingTier":"PRO","trialEnds":"2023-06-16T17:16:37.161Z"}`</span>

<ObjectCollapsible name={"meta"}>

<Property name={"[key: string]"} type={"null"} required={false} deprecated={undefined}>

</Property>

</ObjectCollapsible>

</Property>

<Property name={"roles"} type={"array<string>"} required={false} deprecated={undefined}>

A list of roles that this key should have. If the role does not exist, an error is thrown

<span>Example: `["admin","finance"]`</span>

</Property>

<Property name={"permissions"} type={"array<string>"} required={false} deprecated={undefined}>

A list of permissions that this key should have. If the permission does not exist, an error is thrown

<span>Example: `["domains.create_record","say_hello"]`</span>

</Property>

<Property name={"expires"} type={"integer"} required={false} deprecated={undefined}>

You can auto expire keys by providing a unix timestamp in milliseconds. Once Keys expire they will automatically be disabled and are no longer valid unless you enable them again.

<span>Example: `1623869797161`</span>

</Property>

<Property name={"remaining"} type={"integer"} required={false} deprecated={undefined}>

You can limit the number of requests a key can make. Once a key reaches 0 remaining requests, it will automatically be disabled and is no longer valid unless you update it.

<span>Example: `1000`</span>

<span>Minimum: `1`</span>

</Property>

<Property name={"refill"} type={"object"} required={false} deprecated={undefined}>

Unkey enables you to refill verifications for each key at regular intervals.

<span>Example: `{"interval":"daily","amount":100}`</span>

<ObjectCollapsible name={"refill"}>

<Property name={"interval"} type={"string"} required={true} deprecated={undefined}>

Unkey will automatically refill verifications at the set interval.

<span>Value in: `"daily" | "monthly"`</span>

</Property>

<Property name={"amount"} type={"integer"} required={true} deprecated={undefined}>

The number of verifications to refill for each occurrence is determined individually for each key.

<span>Minimum: `0`</span>

</Property>

</ObjectCollapsible>

</Property>

<Property name={"ratelimit"} type={"object"} required={false} deprecated={undefined}>

Unkey comes with per-key fixed-window ratelimiting out of the box.

<span>Example: `{"type":"fast","limit":10,"duration":60000}`</span>

<ObjectCollapsible name={"ratelimit"}>

<Property name={"async"} type={"boolean"} required={false} deprecated={undefined}>

Async will return a response immediately, lowering latency at the cost of accuracy.

<span>Default: `true`</span>

</Property>

<Property name={"type"} type={"string"} required={false} deprecated={true}>

Deprecated, use `async`. Fast ratelimiting doesn't add latency, while consistent ratelimiting is more accurate.

<span>Default: `"fast"`</span>

<span>Value in: `"fast" | "consistent"`</span>

</Property>

<Property name={"limit"} type={"integer"} required={true} deprecated={undefined}>

The total amount of requests in a given interval.

<span>Minimum: `1`</span>

</Property>

<Property name={"duration"} type={"integer"} required={true} deprecated={undefined}>

The window duration in milliseconds

<span>Example: `60000`</span>

<span>Minimum: `1000`</span>

</Property>

<Property name={"refillRate"} type={"integer"} required={false} deprecated={true}>

How many tokens to refill during each refillInterval.

<span>Minimum: `1`</span>

</Property>

<Property name={"refillInterval"} type={"integer"} required={false} deprecated={true}>

The refill timeframe, in milliseconds.

<span>Minimum: `1`</span>

</Property>

</ObjectCollapsible>

</Property>

<Property name={"enabled"} type={"boolean"} required={false} deprecated={undefined}>

Sets if key is enabled or disabled. Disabled keys are not valid.

<span>Example: `false`</span>

<span>Default: `true`</span>

</Property>

<Property name={"environment"} type={"string"} required={false} deprecated={undefined}>

Environments allow you to divide your keyspace.

Some applications like Stripe, Clerk, WorkOS and others have a concept of "live" and "test" keys to
give the developer a way to develop their own application without the risk of modifying real world
resources.

When you set an environment, we will return it back to you when validating the key, so you can
handle it correctly.
              

<span>Maximum length: `256`</span>

</Property>

</ObjectCollapsible>

</Property>

| Status code | Description |
| ----------- | ----------- |
| `202` | The key ids of all created keys |
| `400` | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |
| `401` | Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response. |
| `403` | The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server. |
| `404` | The server cannot find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web. |
| `409` | This response is sent when a request conflicts with the current state of the server. |
| `429` | The user has sent too many requests in a given amount of time ("rate limiting") |
| `500` | The server has encountered a situation it does not know how to handle. |

<APIPlayground authorization={{"type":"string","name":"authorization","defaultValue":"Bearer","isRequired":true,"description":"The authorization token"}} method={"POST"} route={"/v1/migrations.enqueueKeys"} path={[]} query={[]} header={[]} body={{"type":"object","isRequired":true,"properties":{"migrationId":{"type":"ref","isRequired":true,"schema":"0"},"apiId":{"type":"ref","isRequired":true,"schema":"1"},"keys":{"type":"ref","isRequired":true,"schema":"2"}}}} schemas={{"0":{"type":"string","defaultValue":"","isRequired":false,"description":"Contact support@unkey.dev to receive your migration id."},"1":{"type":"string","defaultValue":"","isRequired":false,"description":"The id of the api, you want to migrate keys to"},"2":{"type":"array","isRequired":false,"items":"3"},"3":{"type":"object","isRequired":false,"properties":{"prefix":{"type":"ref","isRequired":false,"schema":"4"},"name":{"type":"ref","isRequired":false,"schema":"5"},"plaintext":{"type":"ref","isRequired":false,"schema":"6"},"hash":{"type":"ref","isRequired":false,"schema":"7"},"start":{"type":"ref","isRequired":false,"schema":"10"},"ownerId":{"type":"ref","isRequired":false,"schema":"11"},"meta":{"type":"ref","isRequired":false,"schema":"12"},"roles":{"type":"ref","isRequired":false,"schema":"13"},"permissions":{"type":"ref","isRequired":false,"schema":"15"},"expires":{"type":"ref","isRequired":false,"schema":"17"},"remaining":{"type":"ref","isRequired":false,"schema":"18"},"refill":{"type":"ref","isRequired":false,"schema":"19"},"ratelimit":{"type":"ref","isRequired":false,"schema":"22"},"enabled":{"type":"ref","isRequired":false,"schema":"29"},"environment":{"type":"ref","isRequired":false,"schema":"30"}}},"4":{"type":"string","defaultValue":"","isRequired":false,"description":"To make it easier for your users to understand which product an api key belongs to, you can add prefix them.\n\nFor example Stripe famously prefixes their customer ids with cus_ or their api keys with sk_live_.\n\nThe underscore is automatically added if you are defining a prefix, for example: \"prefix\": \"abc\" will result in a key like abc_xxxxxxxxx\n"},"5":{"type":"string","defaultValue":"my key","isRequired":false,"description":"The name for your Key. This is not customer facing."},"6":{"type":"string","defaultValue":"","isRequired":false,"description":"The raw key in plaintext. If provided, unkey encrypts this value and stores it securely. Provide either `hash` or `plaintext`"},"7":{"type":"object","isRequired":false,"description":"Provide either `hash` or `plaintext`","properties":{"value":{"type":"ref","isRequired":true,"schema":"8"},"variant":{"type":"ref","isRequired":true,"schema":"9"}}},"8":{"type":"string","defaultValue":"","isRequired":false,"description":"The hashed and encoded key"},"9":{"type":"string","defaultValue":"","isRequired":false,"description":"The algorithm for hashing and encoding, currently only sha256 and base64 are supported"},"10":{"type":"string","defaultValue":"unkey_32kq","isRequired":false,"description":"The first 4 characters of the key. If a prefix is used, it should be the prefix plus 4 characters."},"11":{"type":"string","defaultValue":"team_123","isRequired":false,"description":"Your user’s Id. This will provide a link between Unkey and your customer record.\nWhen validating a key, we will return this back to you, so you can clearly identify your user from their api key."},"12":{"type":"object","isRequired":false,"description":"This is a place for dynamic meta data, anything that feels useful for you should go here","properties":{}},"13":{"type":"array","description":"A list of roles that this key should have. If the role does not exist, an error is thrown","isRequired":false,"items":"14"},"14":{"type":"string","defaultValue":"","isRequired":false},"15":{"type":"array","description":"A list of permissions that this key should have. If the permission does not exist, an error is thrown","isRequired":false,"items":"16"},"16":{"type":"string","defaultValue":"","isRequired":false},"17":{"type":"number","defaultValue":1623869797161,"isRequired":false,"description":"You can auto expire keys by providing a unix timestamp in milliseconds. Once Keys expire they will automatically be disabled and are no longer valid unless you enable them again."},"18":{"type":"number","defaultValue":1000,"isRequired":false,"description":"You can limit the number of requests a key can make. Once a key reaches 0 remaining requests, it will automatically be disabled and is no longer valid unless you update it."},"19":{"type":"object","isRequired":false,"description":"Unkey enables you to refill verifications for each key at regular intervals.","properties":{"interval":{"type":"ref","isRequired":true,"schema":"20"},"amount":{"type":"ref","isRequired":true,"schema":"21"}}},"20":{"type":"string","defaultValue":"","isRequired":false,"description":"Unkey will automatically refill verifications at the set interval."},"21":{"type":"number","defaultValue":"","isRequired":false,"description":"The number of verifications to refill for each occurrence is determined individually for each key."},"22":{"type":"object","isRequired":false,"description":"Unkey comes with per-key fixed-window ratelimiting out of the box.","properties":{"async":{"type":"ref","isRequired":false,"schema":"23"},"type":{"type":"ref","isRequired":false,"schema":"24"},"limit":{"type":"ref","isRequired":true,"schema":"25"},"duration":{"type":"ref","isRequired":true,"schema":"26"},"refillRate":{"type":"ref","isRequired":false,"schema":"27"},"refillInterval":{"type":"ref","isRequired":false,"schema":"28"}}},"23":{"type":"boolean","defaultValue":"","isRequired":false,"description":"Async will return a response immediately, lowering latency at the cost of accuracy."},"24":{"type":"string","defaultValue":"","isRequired":false,"description":"Deprecated, use `async`. Fast ratelimiting doesn't add latency, while consistent ratelimiting is more accurate."},"25":{"type":"number","defaultValue":"","isRequired":false,"description":"The total amount of requests in a given interval."},"26":{"type":"number","defaultValue":60000,"isRequired":false,"description":"The window duration in milliseconds"},"27":{"type":"number","defaultValue":"","isRequired":false,"description":"How many tokens to refill during each refillInterval."},"28":{"type":"number","defaultValue":"","isRequired":false,"description":"The refill timeframe, in milliseconds."},"29":{"type":"boolean","defaultValue":false,"isRequired":false,"description":"Sets if key is enabled or disabled. Disabled keys are not valid."},"30":{"type":"string","defaultValue":"","isRequired":false,"description":"Environments allow you to divide your keyspace.\n\nSome applications like Stripe, Clerk, WorkOS and others have a concept of \"live\" and \"test\" keys to\ngive the developer a way to develop their own application without the risk of modifying real world\nresources.\n\nWhen you set an environment, we will return it back to you when validating the key, so you can\nhandle it correctly.\n              "}}}>

</APIPlayground>

</APIInfo>

<APIExample>

<Requests items={["cURL","JavaScript"]}>

<Request value={"cURL"}>

```bash
curl -X POST "https://api.unkey.dev/v1/migrations.enqueueKeys" \
  -d '{
  "migrationId": "string",
  "apiId": "string",
  "keys": [
    {
      "prefix": "string",
      "name": "my key",
      "plaintext": "string",
      "hash": {
        "value": "string",
        "variant": "sha256_base64"
      },
      "start": "unkey_32kq",
      "ownerId": "team_123",
      "meta": {
        "billingTier": "PRO",
        "trialEnds": "2023-06-16T17:16:37.161Z"
      },
      "roles": [
        "admin",
        "finance"
      ],
      "permissions": [
        "domains.create_record",
        "say_hello"
      ],
      "expires": 1623869797161,
      "remaining": 1000,
      "refill": {
        "interval": "daily",
        "amount": 100
      },
      "ratelimit": {
        "type": "fast",
        "limit": 10,
        "duration": 60000
      },
      "enabled": false,
      "environment": "string"
    }
  ]
}'
```

</Request>

<Request value={"JavaScript"}>

```js
fetch("https://api.unkey.dev/v1/migrations.enqueueKeys", {
  method: "POST"
});
```

</Request>

</Requests>

<Responses items={["202","400","401","403","404","409","429","500"]}>

<Response value={"202"}>

<ResponseTypes>

<ExampleResponse>

```json
{}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"400"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "BAD_REQUEST",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/BAD_REQUEST",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "BAD_REQUEST";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"401"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/UNAUTHORIZED",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "UNAUTHORIZED";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"403"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "FORBIDDEN",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/FORBIDDEN",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "FORBIDDEN";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"404"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "NOT_FOUND",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/NOT_FOUND",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "NOT_FOUND";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"409"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "CONFLICT",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/CONFLICT",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "CONFLICT";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"429"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "TOO_MANY_REQUESTS",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/TOO_MANY_REQUESTS",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "TOO_MANY_REQUESTS";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"500"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "INTERNAL_SERVER_ERROR",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/INTERNAL_SERVER_ERROR",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "INTERNAL_SERVER_ERROR";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

</Responses>

</APIExample>

</API>

</Root>
`````

## File: packages/openapi/test/out/unkey/ratelimits.mdx
`````
---
title: ratelimits
full: true
---

import { Root, API, APIInfo, APIExample, Responses, Response, ResponseTypes, ExampleResponse, TypeScriptResponse, Property, ObjectCollapsible, Requests, Request, APIPlayground } from "fumadocs-ui/components/api";

<Root baseUrl={"https://api.unkey.dev"}>

<API>

<APIInfo method={"POST"} route={"/v1/ratelimits.limit"}>

## limit

### Authorization

<Property name={"Authorization"} type={"Bearer <token>"} required={true}>

In: `header`

</Property>

### Request Body

<Property name={"namespace"} type={"string"} required={false} deprecated={undefined}>

Namespaces group different limits together for better analytics. You might have a namespace for your public API and one for internal tRPC routes.

<span>Example: `"email.outbound"`</span>

<span>Default: `"default"`</span>

</Property>

<Property name={"identifier"} type={"string"} required={true} deprecated={undefined}>

Identifier of your user, this can be their userId, an email, an ip or anything else.

<span>Example: `"user_123"`</span>

</Property>

<Property name={"limit"} type={"integer"} required={true} deprecated={undefined}>

How many requests may pass in a given window.

<span>Example: `10`</span>

<span>Minimum: `0`</span>

</Property>

<Property name={"duration"} type={"integer"} required={true} deprecated={undefined}>

The window duration in milliseconds

<span>Example: `60000`</span>

<span>Minimum: `1000`</span>

</Property>

<Property name={"cost"} type={"integer"} required={false} deprecated={undefined}>

Expensive requests may use up more tokens. You can specify a cost to the request here and we'll deduct this many tokens in the current window. 
If there are not enough tokens left, the request is denied.
                
Set it to 0 to receive the current limit without changing anything.

<span>Example: `2`</span>

<span>Default: `1`</span>

<span>Minimum: `0`</span>

</Property>

<Property name={"async"} type={"boolean"} required={false} deprecated={undefined}>

Async will return a response immediately, lowering latency at the cost of accuracy.

<span>Default: `false`</span>

</Property>

<Property name={"meta"} type={"object"} required={false} deprecated={undefined}>

Attach any metadata to this request

<ObjectCollapsible name={"meta"}>

<Property name={"[key: string]"} type={"Any properties in string, boolean, number, null, null"} required={false} deprecated={undefined}>

</Property>

</ObjectCollapsible>

</Property>

<Property name={"resources"} type={"array<object>"} required={false} deprecated={undefined}>

Resources that are about to be accessed by the user

<span>Example: `[{"type":"project","id":"p_123","name":"dub"}]`</span>

<ObjectCollapsible name={"Object 1"}>

<Property name={"type"} type={"string"} required={true} deprecated={undefined}>

The type of resource

<span>Example: `"organization"`</span>

</Property>

<Property name={"id"} type={"string"} required={true} deprecated={undefined}>

The unique identifier for the resource

<span>Example: `"org_123"`</span>

</Property>

<Property name={"name"} type={"string"} required={false} deprecated={undefined}>

A human readable name for this resource

<span>Example: `"unkey"`</span>

</Property>

<Property name={"meta"} type={"object"} required={false} deprecated={undefined}>

Attach any metadata to this resources

<ObjectCollapsible name={"meta"}>

<Property name={"[key: string]"} type={"Any properties in string, boolean, number, null, null"} required={false} deprecated={undefined}>

</Property>

</ObjectCollapsible>

</Property>

</ObjectCollapsible>

</Property>

| Status code | Description |
| ----------- | ----------- |
| `200` |  |
| `400` | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |
| `401` | Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response. |
| `403` | The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server. |
| `404` | The server cannot find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web. |
| `409` | This response is sent when a request conflicts with the current state of the server. |
| `429` | The user has sent too many requests in a given amount of time ("rate limiting") |
| `500` | The server has encountered a situation it does not know how to handle. |

<APIPlayground authorization={{"type":"string","name":"authorization","defaultValue":"Bearer","isRequired":true,"description":"The authorization token"}} method={"POST"} route={"/v1/ratelimits.limit"} path={[]} query={[]} header={[]} body={{"type":"object","isRequired":true,"properties":{"namespace":{"type":"ref","isRequired":false,"schema":"0"},"identifier":{"type":"ref","isRequired":true,"schema":"1"},"limit":{"type":"ref","isRequired":true,"schema":"2"},"duration":{"type":"ref","isRequired":true,"schema":"3"},"cost":{"type":"ref","isRequired":false,"schema":"4"},"async":{"type":"ref","isRequired":false,"schema":"5"},"meta":{"type":"ref","isRequired":false,"schema":"6"},"resources":{"type":"ref","isRequired":false,"schema":"7"}}}} schemas={{"0":{"type":"string","defaultValue":"email.outbound","isRequired":false,"description":"Namespaces group different limits together for better analytics. You might have a namespace for your public API and one for internal tRPC routes."},"1":{"type":"string","defaultValue":"user_123","isRequired":false,"description":"Identifier of your user, this can be their userId, an email, an ip or anything else."},"2":{"type":"number","defaultValue":10,"isRequired":false,"description":"How many requests may pass in a given window."},"3":{"type":"number","defaultValue":60000,"isRequired":false,"description":"The window duration in milliseconds"},"4":{"type":"number","defaultValue":2,"isRequired":false,"description":"Expensive requests may use up more tokens. You can specify a cost to the request here and we'll deduct this many tokens in the current window. \nIf there are not enough tokens left, the request is denied.\n                \nSet it to 0 to receive the current limit without changing anything."},"5":{"type":"boolean","defaultValue":"","isRequired":false,"description":"Async will return a response immediately, lowering latency at the cost of accuracy."},"6":{"type":"object","isRequired":false,"description":"Attach any metadata to this request","properties":{}},"7":{"type":"array","description":"Resources that are about to be accessed by the user","isRequired":false,"items":"8"},"8":{"type":"object","isRequired":false,"properties":{"type":{"type":"ref","isRequired":true,"schema":"9"},"id":{"type":"ref","isRequired":true,"schema":"10"},"name":{"type":"ref","isRequired":false,"schema":"11"},"meta":{"type":"ref","isRequired":false,"schema":"12"}}},"9":{"type":"string","defaultValue":"organization","isRequired":false,"description":"The type of resource"},"10":{"type":"string","defaultValue":"org_123","isRequired":false,"description":"The unique identifier for the resource"},"11":{"type":"string","defaultValue":"unkey","isRequired":false,"description":"A human readable name for this resource"},"12":{"type":"object","isRequired":false,"description":"Attach any metadata to this resources","properties":{}}}}>

</APIPlayground>

</APIInfo>

<APIExample>

<Requests items={["cURL","JavaScript"]}>

<Request value={"cURL"}>

```bash
curl -X POST "https://api.unkey.dev/v1/ratelimits.limit" \
  -d '{
  "namespace": "email.outbound",
  "identifier": "user_123",
  "limit": 10,
  "duration": 60000,
  "cost": 2,
  "async": false,
  "meta": {
    "property1": "string",
    "property2": "string"
  },
  "resources": [
    {
      "type": "project",
      "id": "p_123",
      "name": "dub"
    }
  ]
}'
```

</Request>

<Request value={"JavaScript"}>

```js
fetch("https://api.unkey.dev/v1/ratelimits.limit", {
  method: "POST"
});
```

</Request>

</Requests>

<Responses items={["200","400","401","403","404","409","429","500"]}>

<Response value={"200"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "success": true,
  "limit": 10,
  "remaining": 9,
  "reset": 1709804263654
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  /**
   * Returns true if the request should be processed, false if it was rejected.
   */
  success: boolean;
  /**
   * How many requests are allowed within a window.
   */
  limit: number;
  /**
   * How many requests can still be made in the current window.
   */
  remaining: number;
  /**
   * A unix millisecond timestamp when the limits reset.
   */
  reset: number;
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"400"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "BAD_REQUEST",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/BAD_REQUEST",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "BAD_REQUEST";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"401"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/UNAUTHORIZED",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "UNAUTHORIZED";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"403"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "FORBIDDEN",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/FORBIDDEN",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "FORBIDDEN";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"404"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "NOT_FOUND",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/NOT_FOUND",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "NOT_FOUND";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"409"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "CONFLICT",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/CONFLICT",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "CONFLICT";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"429"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "TOO_MANY_REQUESTS",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/TOO_MANY_REQUESTS",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "TOO_MANY_REQUESTS";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

<Response value={"500"}>

<ResponseTypes>

<ExampleResponse>

```json
{
  "error": {
    "code": "INTERNAL_SERVER_ERROR",
    "docs": "https://unkey.dev/docs/api-reference/errors/code/INTERNAL_SERVER_ERROR",
    "message": "string",
    "requestId": "req_1234"
  }
}
```

</ExampleResponse>

<TypeScriptResponse>

```ts
export interface Response {
  error: {
    /**
     * A machine readable error code.
     */
    code: "INTERNAL_SERVER_ERROR";
    /**
     * A link to our documentation with more details about this error code
     */
    docs: string;
    /**
     * A human readable explanation of what went wrong
     */
    message: string;
    /**
     * Please always include the requestId in your error report
     */
    requestId: string;
  };
}
```

</TypeScriptResponse>

</ResponseTypes>

</Response>

</Responses>

</APIExample>

</API>

</Root>
`````

## File: packages/openapi/test/out/petstore.mdx
`````
---
title: Swagger Petstore
full: true
_openapi:
  toc:
    - depth: 2
      title: List all pets
      url: '#list-all-pets'
    - depth: 2
      title: Create a pet
      url: '#create-a-pet'
    - depth: 2
      title: Info for a specific pet
      url: '#info-for-a-specific-pet'
  structuredData:
    headings:
      - content: List all pets
        id: list-all-pets
      - content: Create a pet
        id: create-a-pet
      - content: Info for a specific pet
        id: info-for-a-specific-pet
    contents: []
---

{/* This file was generated by Fumadocs. Do not edit this file directly. Any changes should be made by running the generation command again. */}

<APIPage document={"./fixtures/petstore.yaml"} operations={[{"path":"/pets","method":"get"},{"path":"/pets","method":"post"},{"path":"/pets/{petId}","method":"get"}]} webhooks={[]} hasHead={true} />
`````

## File: packages/openapi/CHANGELOG.md
`````markdown
# @fuma-docs/openapi

## 9.1.4

### Patch Changes

- d449bb1: fix `groupBy: route` ignoring curly braces
- ac33c3c: Add method option and Content-Type header to generated JavaScript code examples
- Updated dependencies [658fa96]
  - fumadocs-core@15.6.5
  - fumadocs-ui@15.6.5

## 9.1.3

### Patch Changes

- Updated dependencies [dca17d7]
  - fumadocs-ui@15.6.4
  - fumadocs-core@15.6.4

## 9.1.2

### Patch Changes

- 742c0a6: fix spacing issues

## 9.1.1

### Patch Changes

- dd94271: Fix handling of primitive types in `anyOf`/`allOf`
- Updated dependencies [a2d7940]
  - fumadocs-ui@15.6.3
  - fumadocs-core@15.6.3

## 9.1.0

### Minor Changes

- b60c8ed: **Support Parameter Serialization**

  Maybe need to update your code if you've added custom media adapters.

### Patch Changes

- Updated dependencies [1e50889]
- Updated dependencies [353c139]
- Updated dependencies [5844c6f]
  - fumadocs-ui@15.6.2
  - fumadocs-core@15.6.2

## 9.0.18

### Patch Changes

- ae38ed0: Fix Scalar `upgrade()` is somehow ignored
- a35597e: Use new codeblock tab style
- 8f69e33: Always display collapsible for array items

## 9.0.17

### Patch Changes

- 7328590: OpenAPI: Fix non-undefined values not rendering
- b606d36: support custom slugify function for generate files

## 9.0.16

### Patch Changes

- Updated dependencies [1a902ff]
  - fumadocs-core@15.6.1
  - fumadocs-ui@15.6.1

## 9.0.15

### Patch Changes

- 504ab2e: Fix minor UI bugs
- Updated dependencies [d0f8a15]
- Updated dependencies [84918b8]
- Updated dependencies [bf15617]
- Updated dependencies [f8d1709]
  - fumadocs-core@15.6.0
  - fumadocs-ui@15.6.0

## 9.0.14

### Patch Changes

- Updated dependencies [e9b1c9c]
- Updated dependencies [d5c9b11]
- Updated dependencies [0d3f76b]
  - fumadocs-ui@15.5.5
  - fumadocs-core@15.5.5

## 9.0.13

### Patch Changes

- Updated dependencies [4a1d3cf]
- Updated dependencies [35c3c0b]
- Updated dependencies [58b7596]
  - fumadocs-ui@15.5.4
  - fumadocs-core@15.5.4

## 9.0.12

### Patch Changes

- b1f805a: Parse body optionally in proxy

## 9.0.11

### Patch Changes

- Updated dependencies [7d1ac21]
  - fumadocs-core@15.5.3
  - fumadocs-ui@15.5.3

## 9.0.10

### Patch Changes

- 7a45921: Add `absolutePath` and `path` properties to pages, mark `file` as deprecated
- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos
- bc7af38: Support C# code example
- 250ab97: Support Java code example
- Updated dependencies [b675728]
- Updated dependencies [7a45921]
- Updated dependencies [1b7bc4b]
- Updated dependencies [82fc4c8]
  - fumadocs-ui@15.5.2
  - fumadocs-core@15.5.2

## 9.0.9

### Patch Changes

- 201235f: Fix trailing slashes being normalized

## 9.0.8

### Patch Changes

- d435088: fix proxy clone request

## 9.0.7

### Patch Changes

- 77461e5: Fix root schema manipulation with TypeScript definition generation

## 9.0.6

### Patch Changes

- 99e3c95: Consistent URL resolution
- Updated dependencies [b4916d2]
- Updated dependencies [8738b9c]
- Updated dependencies [68526ea]
- Updated dependencies [a66886b]
  - fumadocs-core@15.5.1
  - fumadocs-ui@15.5.1

## 9.0.5

### Patch Changes

- 5067efc: Improved support for all OAuth flows
- Updated dependencies [50f8f7f]
- Updated dependencies [589d101]
- Updated dependencies [697d5b4]
  - fumadocs-ui@15.5.0
  - fumadocs-core@15.5.0

## 9.0.4

### Patch Changes

- 9721f6f: Introduce `allowedOrigins` and `filterRequest` options to `createProxy`. Deprecate `allowedUrls` in favour of new APIs.

## 9.0.3

### Patch Changes

- 5770180: Implement multiple security schemes support
- d2a2d47: Skip non-required values when generating code examples
- Updated dependencies [0ab6c7f]
  - fumadocs-core@15.4.2
  - fumadocs-ui@15.4.2

## 9.0.2

### Patch Changes

- 0a90cb9: Improve auth handling
- Updated dependencies [e72b7b4]
  - fumadocs-ui@15.4.1
  - fumadocs-core@15.4.1

## 9.0.1

### Patch Changes

- 2f2ae4d: Disable schema inline on `generateFiles()`
- 951a1a4: Support overriding request/response from `createProxy()`
- 2f2ae4d: Support code samples without `label`
- 2f2ae4d: Hide internal APis since their changes are not documented

## 9.0.0

### Major Changes

- bdef238: **Redesign `generateFiles`**

  This redesign will finalize the behaviour of `generateFiles` to make it simpler, consistent across different versions of Fumadocs OpenAPI.
  - Abandoned `groupByFolder`, it's deprecated long time ago and can be replaced with `groupBy`.
  - Improved type safety, `groupBy` is now only available with `per` set to `operation`.
  - `name` usage changed (see below).

  The `name` option was supposed to designate a output path for generated page. Since `groupBy` was introduced, `name` became somehow useless because its design doesn't work well with `groupBy`.

  **New `name` Design**:

  It now accepts a function:

  ```ts
  generateFiles({
    input: ['./content/docs/openapi/museum.yaml'],
    output: './content/docs/openapi/(generated)',
    per: 'operation',
    name: (output, document) => {
      // page info
      output.item;
      // parsed OpenAPI schema
      document;
      return 'dir/my-file';
    },
  });
  ```

  You can set `algorithm` to `v1` to keep the behaviour of Fumadocs OpenAPI v8:

  ```ts
  generateFiles({
    input: ['./content/docs/openapi/museum.yaml'],
    output: './content/docs/openapi/(generated)',
    per: 'operation',
    name: {
      algorithm: 'v1',
    },
  });
  ```

  `per: operation`:

  File name will be identical with your `operationId` if defined, otherwise fallback to endpoint path or webhook name.

  ```ts
  generateFiles({
    input: ['./content/docs/openapi/museum.yaml'],
    output: './content/docs/openapi/(generated)',
    per: 'operation',
  });
  ```

  With `per: operation`, you can use `groupBy` to group pages:
  - tag: `{tag}/{file}`
  - route: `{endpoint}/{method}` (it will ignore the `name` option)
  - none: `{file}` (default)

  `per: tag | file`:

  They are unchanged.

### Minor Changes

- c945b5f: Mark `mediaAdapters` API stable
- b0c02a0: Redesign schema display UI

### Patch Changes

- 00a81e1: Improve playground body input
- 1bcdc84: Fix recursive reference in `anyOf`/`allOf`/`oneOf`
- Updated dependencies [092fd04]
- Updated dependencies [1b999eb]
- Updated dependencies [961b67e]
- Updated dependencies [7d78bc5]
  - fumadocs-ui@15.4.0
  - fumadocs-core@15.4.0

## 8.1.12

### Patch Changes

- a6c909b: Removed unused devDependencies and migrated from `fast-glob` to `tinyglobby`
- Updated dependencies [e0c2a92]
- Updated dependencies [71fc1a5]
  - fumadocs-ui@15.3.4
  - fumadocs-core@15.3.4

## 8.1.11

### Patch Changes

- Updated dependencies [05b3bd9]
- Updated dependencies [39bf088]
- Updated dependencies [4ae7b4a]
- Updated dependencies [e955a98]
  - fumadocs-ui@15.3.3
  - fumadocs-core@15.3.3

## 8.1.10

### Patch Changes

- 623610a: Improve error message
- Updated dependencies [1753cf1]
- Updated dependencies [9b38baf]
- Updated dependencies [8e862e5]
- Updated dependencies [ac0ab12]
- Updated dependencies [c25d678]
  - fumadocs-ui@15.3.2
  - fumadocs-core@15.3.2

## 8.1.9

### Patch Changes

- Updated dependencies [3372792]
  - fumadocs-core@15.3.1
  - fumadocs-ui@15.3.1

## 8.1.8

### Patch Changes

- Updated dependencies [52b5ad8]
- Updated dependencies [c05dc03]
- Updated dependencies [abce713]
  - fumadocs-ui@15.3.0
  - fumadocs-core@15.3.0

## 8.1.7

### Patch Changes

- 12297de: Lazy load media adapters on client side
- Updated dependencies [50db874]
- Updated dependencies [79e75c3]
  - fumadocs-core@15.2.15
  - fumadocs-ui@15.2.15

## 8.1.6

### Patch Changes

- 3e69302: Support media adapter API
- Updated dependencies [6ea1718]
  - fumadocs-core@15.2.14
  - fumadocs-ui@15.2.14

## 8.1.5

### Patch Changes

- a7ef446: Fix empty directory detection
- Updated dependencies [b433d93]
- Updated dependencies [1e07ed8]
  - fumadocs-ui@15.2.13
  - fumadocs-core@15.2.13

## 8.1.4

### Patch Changes

- 8c67955: Fix duplications with `generateFiles`
- 4b1502e: Improve response type UX
- 47670c8: Support more JSON schema features

## 8.1.3

### Patch Changes

- 67070db: Add missing file
- Updated dependencies [acff667]
- Updated dependencies [b68bb51]
- Updated dependencies [127e681]
  - fumadocs-core@15.2.12
  - fumadocs-ui@15.2.12

## 8.1.2

### Patch Changes

- 2d18405: Support array type in parameters
- 4e62b41: Bundle `lucide-react` as part of library
- Updated dependencies [d4d1ba7]
- Updated dependencies [4e62b41]
- Updated dependencies [07cd690]
  - fumadocs-ui@15.2.11
  - fumadocs-core@15.2.11

## 8.1.1

### Patch Changes

- 4dbb7fb: tolerate array schema without `items` type
- 2625723: Fix infinite rendering on schema
- bd280c8: Change generated file paths for documents

## 8.1.0

### Minor Changes

- bb515b7: Display Response in a separate section

### Patch Changes

- 540027e: **Support `fumadocs-openapi/css/preset.css` for Tailwind CSS**

  We highly recommend to use the following instead:

  ```css
  @import 'tailwindcss';
  @import 'fumadocs-ui/css/neutral.css';
  @import 'fumadocs-ui/css/preset.css';
  /* do this */
  @import 'fumadocs-openapi/css/preset.css';
  ```

- Updated dependencies [3a5595a]
- Updated dependencies [8c9fc1f]
  - fumadocs-ui@15.2.10
  - fumadocs-core@15.2.10

## 8.0.3

### Patch Changes

- Updated dependencies [e72af4b]
- Updated dependencies [ea0f468]
- Updated dependencies [7f3c30e]
  - fumadocs-ui@15.2.9
  - fumadocs-core@15.2.9

## 8.0.2

### Patch Changes

- Updated dependencies [4fad539]
- Updated dependencies [a673ef4]
  - fumadocs-ui@15.2.8
  - fumadocs-core@15.2.8

## 8.0.1

### Patch Changes

- 5a6bf83: fix(#1717): add number type stringify for getPathnameFromInput

## 8.0.0

### Major Changes

- ff12b53: **Move `APIPage` to `fumadocs-openapi/ui`**

  migrate:

  in your `mdx-components.tsx` (or where you pass MDX components):

  ```tsx
  import defaultComponents from 'fumadocs-ui/mdx';
  import { APIPage } from 'fumadocs-openapi/ui';
  import { openapi } from '@/lib/source';
  import type { MDXComponents } from 'mdx/types';

  export function getMDXComponents(components?: MDXComponents): MDXComponents {
    return {
      ...defaultComponents,
      // use this instead
      APIPage: (props) => <APIPage {...openapi.getAPIPageProps(props)} />,
      ...components,
    };
  }
  ```

  why: Next.js compiles the same module in different layers: route handlers, pages (which include browser bundle), and middleware (Edge Runtime). It avoids compiling React components of `fumadocs-openapi` twice when you reference the OpenAPI server in a route handler.

### Patch Changes

- 24ea50d: support JSON mode for body input
- b664784: support `application/x-www-form-urlencoded` content type
- Updated dependencies [eb18da9]
- Updated dependencies [085e39f]
- Updated dependencies [4d50bcf]
- Updated dependencies [ec85a6c]
- Updated dependencies [e1a61bf]
  - fumadocs-ui@15.2.7
  - fumadocs-core@15.2.7

## 7.0.14

### Patch Changes

- Updated dependencies [d49f9ae]
- Updated dependencies [b07e98c]
- Updated dependencies [b07e98c]
- Updated dependencies [3a4bd88]
  - fumadocs-core@15.2.6
  - fumadocs-ui@15.2.6

## 7.0.13

### Patch Changes

- 4d89c13: Improve `generateFiles` warnings
- Updated dependencies [c66ed79]
  - fumadocs-core@15.2.5
  - fumadocs-ui@15.2.5

## 7.0.12

### Patch Changes

- Updated dependencies [1057957]
  - fumadocs-core@15.2.4
  - fumadocs-ui@15.2.4

## 7.0.11

### Patch Changes

- Updated dependencies [5e4e9ec]
- Updated dependencies [293178f]
  - fumadocs-ui@15.2.3
  - fumadocs-core@15.2.3

## 7.0.10

### Patch Changes

- Updated dependencies [0829544]
- Updated dependencies [0829544]
  - fumadocs-ui@15.2.2
  - fumadocs-core@15.2.2

## 7.0.9

### Patch Changes

- 70d7ab0: Change playground `localStorage` key for authorization info
  - fumadocs-ui@15.2.1

## 7.0.8

### Patch Changes

- Updated dependencies [22aeafb]
  - fumadocs-ui@15.2.1
  - fumadocs-core@15.2.1

## 7.0.7

### Patch Changes

- c37b12a: Fix security display issues
- Updated dependencies [c5af09f]
- Updated dependencies [2fd325c]
- Updated dependencies [a7cf4fa]
  - fumadocs-ui@15.2.0
  - fumadocs-core@15.2.0

## 7.0.6

### Patch Changes

- Updated dependencies [b734f92]
  - fumadocs-core@15.1.3
  - fumadocs-ui@15.1.3

## 7.0.5

### Patch Changes

- Updated dependencies [44d5acf]
- Updated dependencies [3f580c4]
  - fumadocs-ui@15.1.2
  - fumadocs-core@15.1.2

## 7.0.4

### Patch Changes

- Updated dependencies [c5add28]
- Updated dependencies [f3cde4f]
- Updated dependencies [7c8a690]
- Updated dependencies [b812457]
  - fumadocs-core@15.1.1
  - fumadocs-ui@15.1.1

## 7.0.3

### Patch Changes

- Updated dependencies [f491f6f]
- Updated dependencies [f491f6f]
- Updated dependencies [f491f6f]
  - fumadocs-core@15.1.0
  - fumadocs-ui@15.1.0

## 7.0.2

### Patch Changes

- 30b7bd4: Fix codeblock highlight options being ignored
- Updated dependencies [e7e2a2a]
  - fumadocs-ui@15.0.18
  - fumadocs-core@15.0.18

## 7.0.1

### Patch Changes

- Updated dependencies [b790699]
- Updated dependencies [72f79cf]
  - fumadocs-ui@15.0.17
  - fumadocs-core@15.0.17

## 7.0.0

### Major Changes

- 190ec35: Auto-update generated API example as user interact with API Playground

### Minor Changes

- 670c179: Support cookie parameters

### Patch Changes

- fumadocs-core@15.0.16
- fumadocs-ui@15.0.16

## 7.0.0-beta.0

### Major Changes

- Auto-update generated API example as user interact with API Playground

## 6.3.0

### Minor Changes

- 70d715d: Added auto-generated comments to top of generated openapi docs files

### Patch Changes

- Updated dependencies [9f6d39a]
- Updated dependencies [0e5e14d]
- Updated dependencies [2035cb1]
  - fumadocs-core@15.0.15
  - fumadocs-ui@15.0.15

## 6.2.1

### Patch Changes

- Updated dependencies [37dc0a6]
- Updated dependencies [796cc5e]
- Updated dependencies [2cc0be5]
- Updated dependencies [6bc033a]
  - fumadocs-core@15.0.14
  - fumadocs-ui@15.0.14

## 6.2.0

### Minor Changes

- ecf7288: Support OAuth 2.0 in-browser authorize dialog

### Patch Changes

- Updated dependencies [7608f4e]
- Updated dependencies [89ff3ae]
- Updated dependencies [16c8944]
  - fumadocs-ui@15.0.13
  - fumadocs-core@15.0.13

## 6.1.1

### Patch Changes

- 3534a10: Move `fumadocs-core` highlighting utils to `fumadocs-core/highlight` and `fumadocs-core/highlight/client`
- Updated dependencies [3534a10]
- Updated dependencies [ecacb53]
- Updated dependencies [93952db]
  - fumadocs-core@15.0.12
  - fumadocs-ui@15.0.12

## 6.1.0

### Minor Changes

- 3d211f3: throw error, when input file is not found

### Patch Changes

- 5730116: Improve experience to customise API Playground
- Updated dependencies [886da49]
- Updated dependencies [04e6c6e]
  - fumadocs-ui@15.0.11
  - fumadocs-core@15.0.11

## 6.0.11

### Patch Changes

- 0a13c45: Support response examples
- Updated dependencies [e8a3ab7]
- Updated dependencies [d95c21f]
  - fumadocs-ui@15.0.10
  - fumadocs-core@15.0.10

## 6.0.10

### Patch Changes

- Updated dependencies [fa5b908]
  - fumadocs-ui@15.0.9
  - fumadocs-core@15.0.9

## 6.0.9

### Patch Changes

- Updated dependencies [8f5993b]
  - fumadocs-ui@15.0.8
  - fumadocs-core@15.0.8

## 6.0.8

### Patch Changes

- f118e24: Fix gaps of property components under parameters section
- Updated dependencies [5deaf40]
- Updated dependencies [f782c2c]
  - fumadocs-core@15.0.7
  - fumadocs-ui@15.0.7

## 6.0.7

### Patch Changes

- e7b6f0a: Support `disablePlayground` option
- Updated dependencies [08236e1]
- Updated dependencies [a06af26]
  - fumadocs-core@15.0.6
  - fumadocs-ui@15.0.6

## 6.0.6

### Patch Changes

- Updated dependencies [14b2f95]
  - fumadocs-ui@15.0.5
  - fumadocs-core@15.0.5

## 6.0.5

### Patch Changes

- c892bd9: fix(packages/openapi): hide AuthSection is security is an empty array
- cd894b1: Feat: support multiple examples in openapi operation #1370

  Adds two new options to the ApiExample renderer "Samples" and "Sample"

- 31e7e3e: Improve sample select UI
- Updated dependencies [c892bd9]
- Updated dependencies [c892bd9]
  - fumadocs-ui@15.0.4
  - fumadocs-core@15.0.4

## 6.0.4

### Patch Changes

- f3ccad2: fix: openapi - preserve <> placeholder marker for params with no example value
- ff9bf0f: Fix: Hide the server select panel, not just the select, if no or only one server is present
- Updated dependencies [47171db]
  - fumadocs-ui@15.0.3
  - fumadocs-core@15.0.3

## 6.0.3

### Patch Changes

- a8e9e1f: Bump deps
- ab44e05: Add file extensions to imports
- Updated dependencies [a8e9e1f]
  - fumadocs-ui@15.0.2
  - fumadocs-core@15.0.2

## 6.0.2

### Patch Changes

- a127dc4: Move to `tsc` for building package
- Updated dependencies [421166a]
  - fumadocs-ui@15.0.1
  - fumadocs-core@15.0.1

## 6.0.1

### Patch Changes

- 127d9df: Fix type errors

## 6.0.0

### Major Changes

- 1286a04: **Change interface for `useScalar`**

  From:

  ```tsx
  import { createOpenAPI } from 'fumadocs-openapi/server';
  import { APIPlayground } from 'fumadocs-openapi/scalar';

  export const openapi = createOpenAPI({
    useScalar: true,
  });
  ```

  To:

  ```tsx
  import { createOpenAPI } from 'fumadocs-openapi/server';
  import { APIPlayground } from 'fumadocs-openapi/scalar';

  export const openapi = createOpenAPI({
    renderer: {
      APIPlayground,
    },
  });
  ```

### Minor Changes

- 9e02460: Add built-in UI to basic auth input (username:password)

## 5.12.0

### Minor Changes

- 471478b: Support `useScalar` option

### Patch Changes

- 983b8a6: Use path of operation when id is not defined
- Updated dependencies [5b8cca8]
- Updated dependencies [a89d6e0]
- Updated dependencies [a84f37a]
- Updated dependencies [f2f9c3d]
- Updated dependencies [a763058]
- Updated dependencies [581f4a5]
  - fumadocs-core@15.0.0
  - fumadocs-ui@15.0.0

## 5.11.8

### Patch Changes

- Updated dependencies [4f2538a]
- Updated dependencies [191012a]
- Updated dependencies [fb6b168]
  - fumadocs-ui@14.7.7
  - fumadocs-core@14.7.7

## 5.11.7

### Patch Changes

- b9601fb: Update Shiki
- Updated dependencies [b9601fb]
  - fumadocs-core@14.7.6
  - fumadocs-ui@14.7.6

## 5.11.6

### Patch Changes

- Updated dependencies [5d41bf1]
- Updated dependencies [777188b]
- Updated dependencies [900eb6c]
- Updated dependencies [a959374]
  - fumadocs-ui@14.7.5
  - fumadocs-core@14.7.5

## 5.11.5

### Patch Changes

- Updated dependencies [26d9ccb]
- Updated dependencies [036f8e1]
- Updated dependencies [bb73a72]
- Updated dependencies [69bd4fe]
  - fumadocs-ui@14.7.4
  - fumadocs-core@14.7.4

## 5.11.4

### Patch Changes

- 056ab2c: Add `showResponseSchema` option to show the full response schema
- Updated dependencies [041f230]
- Updated dependencies [ca1cf19]
  - fumadocs-core@14.7.3
  - fumadocs-ui@14.7.3

## 5.11.3

### Patch Changes

- 35a12cd: Add code sample generation support for variable url

## 5.11.2

### Patch Changes

- 60fe635: Support variable server url
- Updated dependencies [14b280c]
  - fumadocs-core@14.7.2
  - fumadocs-ui@14.7.2

## 5.11.1

### Patch Changes

- Updated dependencies [72dc093]
- Updated dependencies [18b00c1]
  - fumadocs-core@14.7.1
  - fumadocs-ui@14.7.1

## 5.11.0

### Minor Changes

- 0e8be0e: Support XML request body

### Patch Changes

- 698b385: Fix switcher default value being ignored
- Updated dependencies [a557bb4]
- Updated dependencies [97ed36c]
  - fumadocs-ui@14.7.0
  - fumadocs-core@14.7.0

## 5.10.6

### Patch Changes

- Updated dependencies [e95be52]
- Updated dependencies [f3298ea]
  - fumadocs-ui@14.6.8
  - fumadocs-core@14.6.8

## 5.10.5

### Patch Changes

- Updated dependencies [5474343]
  - fumadocs-core@14.6.7
  - fumadocs-ui@14.6.7

## 5.10.4

### Patch Changes

- Updated dependencies [9c930ea]
  - fumadocs-ui@14.6.6
  - fumadocs-core@14.6.6

## 5.10.3

### Patch Changes

- Updated dependencies [969da26]
  - fumadocs-core@14.6.5
  - fumadocs-ui@14.6.5

## 5.10.2

### Patch Changes

- Updated dependencies [b71064a]
- Updated dependencies [67124b1]
- Updated dependencies [1810868]
  - fumadocs-core@14.6.4
  - fumadocs-ui@14.6.4

## 5.10.1

### Patch Changes

- Updated dependencies [abc3677]
  - fumadocs-ui@14.6.3
  - fumadocs-core@14.6.3

## 5.10.0

### Minor Changes

- 8aff7f4: Support Route Handler Proxy

### Patch Changes

- 1a2597a: Expose `--fd-tocnav-height` CSS variable
- Updated dependencies [9908922]
- Updated dependencies [2357d40]
- Updated dependencies [ece734f]
- Updated dependencies [1a2597a]
  - fumadocs-ui@14.6.2
  - fumadocs-core@14.6.2

## 5.9.0

### Minor Changes

- ec5fb2e: Replace `@apidevtools/json-schema-ref-parser` with `@scalar/openapi-parser`

### Patch Changes

- Updated dependencies [9532855]
  - fumadocs-ui@14.6.1
  - fumadocs-core@14.6.1

## 5.8.2

### Patch Changes

- 4766292: Support React 19
- Updated dependencies [010da9e]
- Updated dependencies [bebb16b]
- Updated dependencies [9585561]
- Updated dependencies [4dfde6b]
- Updated dependencies [bebb16b]
- Updated dependencies [4766292]
- Updated dependencies [050b326]
  - fumadocs-ui@14.6.0
  - fumadocs-core@14.6.0

## 5.8.1

### Patch Changes

- Updated dependencies [b7745f4]
- Updated dependencies [9a18c14]
  - fumadocs-ui@14.5.6
  - fumadocs-core@14.5.6

## 5.8.0

### Minor Changes

- 2d0501f: Support webhooks & callbacks
- 2d0501f: Support OpenAPI 3.1

### Patch Changes

- Updated dependencies [06f66d8]
- Updated dependencies [2d0501f]
  - fumadocs-ui@14.5.5
  - fumadocs-core@14.5.5

## 5.7.5

### Patch Changes

- Updated dependencies [8e2cb31]
  - fumadocs-ui@14.5.4
  - fumadocs-core@14.5.4

## 5.7.4

### Patch Changes

- Updated dependencies [c5a5ba0]
- Updated dependencies [f34e895]
- Updated dependencies [4c82a3d]
- Updated dependencies [f8e5157]
- Updated dependencies [ad00dd3]
  - fumadocs-ui@14.5.3
  - fumadocs-core@14.5.3

## 5.7.3

### Patch Changes

- Updated dependencies [072e349]
  - fumadocs-ui@14.5.2
  - fumadocs-core@14.5.2

## 5.7.2

### Patch Changes

- Updated dependencies [6fd480f]
  - fumadocs-ui@14.5.1
  - fumadocs-core@14.5.1

## 5.7.1

### Patch Changes

- Updated dependencies [66c70ec]
- Updated dependencies [05d224c]
  - fumadocs-ui@14.5.0
  - fumadocs-core@14.5.0

## 5.7.0

### Minor Changes

- c66df64: OpenAPI: Display the server selector only when more than one server is defined in the OpenAPI schema
  OpenAPI: Improve APIInfo position for better visibility on smaller screens

## 5.6.2

### Patch Changes

- Updated dependencies [0f1603a]
  - fumadocs-ui@14.4.2
  - fumadocs-core@14.4.2

## 5.6.1

### Patch Changes

- Updated dependencies [07474cb]
- Updated dependencies [48a2c15]
  - fumadocs-ui@14.4.1
  - fumadocs-core@14.4.1

## 5.6.0

### Minor Changes

- 196b78b: OpenAPI: Server selector to allow interacting with different API environments

## 5.5.11

### Patch Changes

- 47fc20e: Fix custom name in `apiKey` type authorization being ignored

## 5.5.10

### Patch Changes

- Updated dependencies [5fd4e2f]
- Updated dependencies [5fd4e2f]
- Updated dependencies [5145123]
- Updated dependencies [64defe0]
- Updated dependencies [8a3f5b0]
  - fumadocs-ui@14.4.0
  - fumadocs-core@14.4.0

## 5.5.9

### Patch Changes

- Updated dependencies [e7443d7]
  - fumadocs-ui@14.3.1
  - fumadocs-core@14.3.1

## 5.5.8

### Patch Changes

- 4e76165: Fix rendering of OpenAPI nullable defined with `allOf`.
- Updated dependencies [80655b3]
- Updated dependencies [b8a12ed]
  - fumadocs-ui@14.3.0
  - fumadocs-core@14.3.0

## 5.5.7

### Patch Changes

- Updated dependencies [ca94bfd]
- Updated dependencies [2949da3]
  - fumadocs-core@14.2.1
  - fumadocs-ui@14.2.1

## 5.5.6

### Patch Changes

- Updated dependencies [e248a0f]
- Updated dependencies [7a5393b]
  - fumadocs-core@14.2.0
  - fumadocs-ui@14.2.0

## 5.5.5

### Patch Changes

- Updated dependencies [1573d63]
  - fumadocs-core@14.1.1
  - fumadocs-ui@14.1.1

## 5.5.4

### Patch Changes

- d6d290c: Upgrade Shiki
- d50750b: Improved UI design
- Updated dependencies [b262d99]
- Updated dependencies [d6d290c]
- Updated dependencies [4a643ff]
- Updated dependencies [b262d99]
- Updated dependencies [90725c1]
  - fumadocs-core@14.1.0
  - fumadocs-ui@14.1.0

## 5.5.3

### Patch Changes

- 35695be: Support multiple tags in OpenAPI `groupBy: tag` file generation

## 5.5.2

### Patch Changes

- Updated dependencies [bfc2bf2]
  - fumadocs-ui@14.0.2
  - fumadocs-core@14.0.2

## 5.5.1

### Patch Changes

- Updated dependencies [1a7d78a]
  - fumadocs-ui@14.0.1
  - fumadocs-core@14.0.1

## 5.5.0

### Minor Changes

- 129923e: Support custom `shiki` options
- 160e52e: Support `disableCache` prop on APIPage

### Patch Changes

- 61a3d14: Support `x-displayName` on tags
- e612f2a: Make compatible with Next.js 15
- 8a32f79: Fix header name in code samples
- be820c4: Bump deps
- 42c9701: Fix TypeScript schema generation
- Updated dependencies [e45bc67]
- Updated dependencies [34cf456]
- Updated dependencies [d9e908e]
- Updated dependencies [d9e908e]
- Updated dependencies [d9e908e]
- Updated dependencies [f949520]
- Updated dependencies [ad47fd8]
- Updated dependencies [9a0b09f]
- Updated dependencies [9a0b09f]
- Updated dependencies [d9e908e]
- Updated dependencies [367f4c3]
- Updated dependencies [87063eb]
- Updated dependencies [367f4c3]
- Updated dependencies [64f0653]
- Updated dependencies [e1ee822]
- Updated dependencies [d9e908e]
- Updated dependencies [d9e908e]
- Updated dependencies [e612f2a]
- Updated dependencies [3d0369a]
- Updated dependencies [9a0b09f]
- Updated dependencies [d9e908e]
- Updated dependencies [9a10262]
- Updated dependencies [d9e908e]
- Updated dependencies [3d054a8]
- Updated dependencies [8ef00dc]
- Updated dependencies [979e301]
- Updated dependencies [d9e908e]
- Updated dependencies [979e301]
- Updated dependencies [15781f0]
- Updated dependencies [be820c4]
- Updated dependencies [be53a0e]
- Updated dependencies [d9e908e]
  - fumadocs-core@14.0.0
  - fumadocs-ui@14.0.0

## 5.4.14

### Patch Changes

- Updated dependencies [6231ad3]
- Updated dependencies [4cb74d5]
  - fumadocs-core@13.4.10
  - fumadocs-ui@13.4.10

## 5.4.13

### Patch Changes

- Updated dependencies [083f04a]
- Updated dependencies [bcf51a6]
  - fumadocs-core@13.4.9
  - fumadocs-ui@13.4.9

## 5.4.12

### Patch Changes

- Updated dependencies [5581733]
- Updated dependencies [78e59e7]
- Updated dependencies [1a327cc]
  - fumadocs-ui@13.4.8
  - fumadocs-core@13.4.8

## 5.4.11

### Patch Changes

- Updated dependencies [6e1923e]
- Updated dependencies [6e1923e]
- Updated dependencies [6e1923e]
  - fumadocs-core@13.4.7
  - fumadocs-ui@13.4.7

## 5.4.10

### Patch Changes

- Updated dependencies [b33aff0]
- Updated dependencies [afb697e]
- Updated dependencies [6bcd263]
- Updated dependencies [daa66d2]
  - fumadocs-ui@13.4.6
  - fumadocs-core@13.4.6

## 5.4.9

### Patch Changes

- 5bca46f: Support removing all code samples
- Updated dependencies [d46a3f1]
  - fumadocs-ui@13.4.5
  - fumadocs-core@13.4.5

## 5.4.8

### Patch Changes

- Updated dependencies [729928e]
  - fumadocs-core@13.4.4
  - fumadocs-ui@13.4.4

## 5.4.7

### Patch Changes

- fumadocs-core@13.4.3
- fumadocs-ui@13.4.3

## 5.4.6

### Patch Changes

- 0cff470: Enable group id on tabs by default
- 0c251e5: Bump deps
- Updated dependencies [7dabbc1]
- Updated dependencies [0c251e5]
- Updated dependencies [3b56170]
- Updated dependencies [0c251e5]
- Updated dependencies [0c251e5]
  - fumadocs-core@13.4.2
  - fumadocs-ui@13.4.2

## 5.4.5

### Patch Changes

- Updated dependencies [95dbba1]
  - fumadocs-core@13.4.1
  - fumadocs-ui@13.4.1

## 5.4.4

### Patch Changes

- Updated dependencies [26f5360]
  - fumadocs-ui@13.4.0
  - fumadocs-core@13.4.0

## 5.4.3

### Patch Changes

- Updated dependencies [f8cc167]
  - fumadocs-core@13.3.3
  - fumadocs-ui@13.3.3

## 5.4.2

### Patch Changes

- 3d1ec96: Improve schema fields margins

## 5.4.1

### Patch Changes

- 029a156: Fix `display` on property components
- eb922e1: Support adding `description` to generated document body

## 5.4.0

### Minor Changes

- 6cf5535: Persist `authorization` field

## 5.3.2

### Patch Changes

- 0b93a31: Support `required` in `allOf` schemas

## 5.3.1

### Patch Changes

- 5660e1e: Fix `allOf` schema display problem
- 28bb673: Fix fields styles

## 5.3.0

### Minor Changes

- 3fa2436: Support Python code sample

### Patch Changes

- 3e4627a: Show required label on body parameters
- 10f6f39: Fix common parameters
- Updated dependencies [17746a6]
- Updated dependencies [0e0ef8c]
  - fumadocs-ui@13.3.2
  - fumadocs-core@13.3.2

## 5.2.2

### Patch Changes

- Updated dependencies [7258c4b]
  - fumadocs-ui@13.3.1
  - fumadocs-core@13.3.1

## 5.2.1

### Patch Changes

- 81d0887: Support disabling code sample with undefined source
- Updated dependencies [8f5b19e]
- Updated dependencies [4916f84]
- Updated dependencies [fd46eb6]
- Updated dependencies [fd46eb6]
- Updated dependencies [fd46eb6]
- Updated dependencies [fd46eb6]
- Updated dependencies [32ca37a]
- Updated dependencies [9aae448]
- Updated dependencies [c542561]
  - fumadocs-ui@13.3.0
  - fumadocs-core@13.3.0

## 5.2.0

### Minor Changes

- 70172f1: Change default value of `per` to `operation`

### Patch Changes

- 61b91fa: Improve Fumadocs OpenAPI support
- Updated dependencies [36b771b]
- Updated dependencies [61b91fa]
  - fumadocs-core@13.2.2
  - fumadocs-ui@13.2.2

## 5.1.0

### Minor Changes

- c7aa090: Generate `document` field on output MDX files

### Patch Changes

- Updated dependencies [17fa173]
  - fumadocs-core@13.2.1
  - fumadocs-ui@13.2.1

## 5.0.3

### Patch Changes

- 96c9dda: Change Heading scroll margins
- c094fef: Fix compatibility issues on other content sources
- Updated dependencies [96c9dda]
- Updated dependencies [ba588a2]
- Updated dependencies [96c9dda]
- Updated dependencies [ec983a3]
  - fumadocs-core@13.2.0
  - fumadocs-ui@13.2.0

## 5.0.2

### Patch Changes

- 22549cd: Add authorization properties to examples

## 5.0.1

### Patch Changes

- 444af27: Fix self-referencing schema types
- 90af678: Reduce initial loaded bundle size

## 5.0.0

### Major Changes

- 971817c: **Migrate to React Server Component**

  The API reference page is now a server component.
  The MDX generator will only generate a small MDX file, and the rest will be handled by our `APIPage` component.

  ```mdx
  ---
  title: Delete Api
  full: true
  method: POST
  route: /v1/apis.deleteApi
  ---

  <APIPage
    operations={[{ path: '/v1/apis.deleteApi', method: 'post' }]}
    hasHead={false}
  />
  ```

  - Markdown/MDX content is still supported, but will be processed in the server component (during runtime) instead.
  - Your Remark/Rehype plugins (e.g. Rehype Code) configured in Fumadocs MDX or other source providers, will **not** be shared. Fumadocs OpenAPI uses a separate MDX processor instance.
  - `APIPage` component will fetch the OpenAPI Schema when being rendered. **On Vercel**, if it relies on the file system, ensure the page **will not** be re-rendered after build.

  Please refer to documentation for the new usage.

### Minor Changes

- 480d211: Change output path logic
- 4bf9851: Support to group pages by tags
- 3874ab5: Support Go Sample Request
- 3874ab5: Replace Response Table of Tabs

### Patch Changes

- 4bf9851: Improve Curl example generator
- Updated dependencies [f280191]
- Updated dependencies [61ef42c]
- Updated dependencies [deae4dd]
- Updated dependencies [c8910c4]
- Updated dependencies [c8910c4]
- Updated dependencies [6c42960]
  - fumadocs-core@13.1.0
  - fumadocs-ui@13.1.0

## 4.4.2

### Patch Changes

- Updated dependencies [37bbfff]
- Updated dependencies [e7c52f2]
  - fumadocs-core@13.0.7
  - fumadocs-ui@13.0.7

## 4.4.1

### Patch Changes

- Updated dependencies [1622e36]
  - fumadocs-ui@13.0.6
  - fumadocs-core@13.0.6

## 4.4.0

### Minor Changes

- b109e44: Improve generated sample requests

### Patch Changes

- Updated dependencies [2cf65f6]
  - fumadocs-core@13.0.5
  - fumadocs-ui@13.0.5

## 4.3.1

### Patch Changes

- d987912: Show current request pathname in Playground
- 0146572: Fix empty params

## 4.3.0

### Minor Changes

- 5acebdd: Support grouping output by folders (per operation)
- 744bd24: Support accessing context information on custom frontmatter
- 6bb9d2d: Support integration with Fumadocs Source API

### Patch Changes

- 744bd24: Fix generate files on `operation` mode
- Updated dependencies [5355391]
  - fumadocs-core@13.0.4
  - fumadocs-ui@13.0.4

## 4.2.2

### Patch Changes

- Updated dependencies [978342f]
  - fumadocs-core@13.0.3
  - fumadocs-ui@13.0.3

## 4.2.1

### Patch Changes

- Updated dependencies [4819820]
  - fumadocs-core@13.0.2
  - fumadocs-ui@13.0.2

## 4.2.0

### Minor Changes

- dfcc61f: Implement multipart form data

### Patch Changes

- f2b540a: Fix `fetch` problems on API Playground

## 4.1.1

### Patch Changes

- fumadocs-core@13.0.1
- fumadocs-ui@13.0.1

## 4.1.0

### Minor Changes

- abf84bb: Support to customise/disable TypeScript Response generation
- 40728a1: Support custom fields (auth, query, header, path and body)

### Patch Changes

- Updated dependencies [89190ae]
- Updated dependencies [b02eebf]
- Updated dependencies [09c3103]
- Updated dependencies [f868018]
- Updated dependencies [8aebeab]
- Updated dependencies [c684c00]
- Updated dependencies [8aebeab]
- Updated dependencies [0377bb4]
- Updated dependencies [e8e6a17]
- Updated dependencies [c8964d3]
- Updated dependencies [c901e6b]
- Updated dependencies [daa7d3c]
- Updated dependencies [c714eaa]
- Updated dependencies [89190ae]
- Updated dependencies [b02eebf]
- Updated dependencies [b02eebf]
- Updated dependencies [4373231]
  - fumadocs-ui@13.0.0
  - fumadocs-core@13.0.0

## 4.0.6

### Patch Changes

- Updated dependencies [a332bee]
  - fumadocs-ui@12.5.6
  - fumadocs-core@12.5.6

## 4.0.5

### Patch Changes

- Updated dependencies [3519e6c]
  - fumadocs-ui@12.5.5
  - fumadocs-core@12.5.5

## 4.0.4

### Patch Changes

- Updated dependencies [fccdfdb]
- Updated dependencies [2ffd5ea]
  - fumadocs-core@12.5.4
  - fumadocs-ui@12.5.4

## 4.0.3

### Patch Changes

- Updated dependencies [5d963f4]
  - fumadocs-ui@12.5.3

## 4.0.2

### Patch Changes

- 0c8eddf: Fix overlap of navbar and api info
- Updated dependencies [a5c34f0]
  - fumadocs-ui@12.5.2

## 4.0.1

### Patch Changes

- Updated dependencies [c5d20d0]
- Updated dependencies [3d8f6cf]
  - fumadocs-ui@12.5.1

## 4.0.0

### Major Changes

- ad143e1: Move UI implementation from `fumadocs-ui` to `fumadocs-openapi`.

  **why:** Allow a better organization of packages.

  **migrate:**

  This package is now Tailwind CSS only, you need to use it in conjunction with the official Tailwind CSS plugin.

  Add the package to `content` under your Tailwind CSS configuration.

  ```js
  import { createPreset, presets } from 'fumadocs-ui/tailwind-plugin';

  /** @type {import('tailwindcss').Config} */
  export default {
    content: [
      './node_modules/fumadocs-ui/dist/**/*.js',
      './node_modules/fumadocs-openapi/dist/**/*.js',
    ],
    presets: [createPreset()],
  };
  ```

  Re-generate MDX files if needed.

### Minor Changes

- ad143e1: Implement OpenAPI playground
- ad143e1: Support passing base url to Root component

### Patch Changes

- ad143e1: Combine `allOf` into one object schema
- Updated dependencies [b9fa99d]
- Updated dependencies [a4bcaa7]
- Updated dependencies [d1c7405]
  - fumadocs-ui@12.5.0

## 3.3.0

### Minor Changes

- b1b154e: Display object types mentioned in schema
- 81fde3f: Support complex types & self-referencing types

## 3.2.0

### Minor Changes

- 0e420cb: Support generating custom code examples

## 3.1.3

### Patch Changes

- 464e44c: Improve example request URL generation

## 3.1.2

### Patch Changes

- 78acd55: Use full mode on docs pages by default on OpenAPI generated pages

## 3.1.1

### Patch Changes

- 318eaf9: Support generating files per operation

## 3.1.0

### Minor Changes

- 3bdc786: Support JavaScript request example
- 3bdc786: Support generating Authorization (`security`) section

## 3.0.0

### Major Changes

- 284a571: **Renew Generate API.**

  **why:** Improve flexibility.

  **migrate:**

  Removed the `render` option from `generate`, `generateFiles` and `generateTags`, use `frontmatter` to customise frontmatter, `imports` to customise imports.

- 284a571: **Support Custom MDX Renderer.**

  **why:** Allow people to customise how the MDX file is generated.

  **migrate:**

  Changed the output of MDX files, the new structure requires components:
  - Root
  - API
  - APIInfo
  - APIExample
  - Responses
  - Response
  - ExampleResponse
  - TypeScriptResponse
  - Property
  - ObjectCollapsible
  - ResponseTypes

  ````mdx
  <API>

  <APIInfo method={"GET"} route={"/pets/{petId}"}>

  ## Info for a specific pet

  ### Path Parameters

  <Property name={"petId"} type={"string"} required={true} deprecated={false}>

  The id of the pet to retrieve

  </Property>

  | Status code | Description                          |
  | ----------- | ------------------------------------ |
  | `200`       | Expected response to a valid request |
  | `default`   | unexpected error                     |

  </APIInfo>

  <APIExample>

  ```bash title="curl"
  curl -X GET "http://petstore.swagger.io/pets/string"
  ```

  <Responses items={["200","default"]}>

  <Response value={"200"}>

  <ResponseTypes>

  <ExampleResponse>

  ```json
  {
    "id": 0,
    "name": "string",
    "tag": "string"
  }
  ```

  </ExampleResponse>

  <TypeScriptResponse>

  ```ts
  export interface Response {
    id: number;
    name: string;
    tag?: string;
  }
  ```

  </TypeScriptResponse>

  </ResponseTypes>

  </Responses>

  </APIExample>

  </API>
  ````

## 2.0.5

### Patch Changes

- bcc05d6: Fix docs typo

## 2.0.4

### Patch Changes

- 310e0ab: Fix multi-line frontmatter

## 2.0.3

### Patch Changes

- 1d3917f: Fix nullable types cannot be detected

## 2.0.2

### Patch Changes

- 9681cc3: Add put method key

## 2.0.1

### Patch Changes

- 8ef2b68: Bump deps

## 2.0.0

### Major Changes

- eacd7b0b: **Remove support for bin usages**

  why: It is more flexible and faster to write a script directly.

  migrate: Create a script named `scripts/generate-docs.mjs`:

  ```js
  import { generateFiles } from 'fumadocs-openapi';

  void generateFiles({
    input: ['./petstore.yaml'],
    output: './content/docs',
  });
  ```

  Execute it with `node ./scripts/generate-docs.mjs`.

## 1.1.0

### Minor Changes

- 8665888: Added patterns support to config Inputs.

## 1.0.1

### Patch Changes

- 6c5a39a: Rename Git repository to `fumadocs`

## 1.0.0

### Major Changes

- 2b11c20: **Rename to Fumadocs**

  `next-docs-zeta` -> `fumadocs-core`

  `next-docs-ui` -> `fumadocs-ui`

  `next-docs-mdx` -> `fumadocs-mdx`

  `@fuma-docs/openapi` -> `fumadocs-openapi`

  `create-next-docs-app` -> `create-fumadocs-app`

## 0.1.0

### Minor Changes

- 45a52ae: **Support generating docs for OpenAPI schema**

  In `openapi.config.js`:

  ```js
  /**
   * @type {import("@fuma-docs/openapi").Config}
   */
  module.exports = {
    input: ['./petstore.yaml'],
    output: './content/docs',
    per: 'tag',
    render: (title, description) => {
      return {
        frontmatter: [
          '---',
          `title: ${title}`,
          `description: ${description}`,
          'toc: false',
          '---',
        ].join('\n'),
      };
    },
  };
  ```

  Run `fuma-docs-openapi` to generate.
`````

## File: packages/python/CHANGELOG.md
`````markdown
# fumadocs-python

## 0.0.3

### Patch Changes

- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos
- Updated dependencies [b675728]
- Updated dependencies [7a45921]
- Updated dependencies [1b7bc4b]
- Updated dependencies [82fc4c8]
  - fumadocs-ui@15.5.2
  - fumadocs-core@15.5.2

## 0.0.2

### Patch Changes

- b0fa6ac: Fix: Add missing dependency for `griffe_typingdoc`
- Updated dependencies [3372792]
  - fumadocs-core@15.3.1
  - fumadocs-ui@15.3.1

## 0.0.1

### Patch Changes

- 3eef0bd: Initial release
- Updated dependencies [d4d1ba7]
- Updated dependencies [4e62b41]
- Updated dependencies [07cd690]
  - fumadocs-ui@15.2.11
  - fumadocs-core@15.2.11
`````

## File: packages/twoslash/CHANGELOG.md
`````markdown
# fumadocs-twoslash

## 3.1.4

### Patch Changes

- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos
- Updated dependencies [b675728]
- Updated dependencies [1b7bc4b]
- Updated dependencies [82fc4c8]
  - fumadocs-ui@15.5.2

## 3.1.3

### Patch Changes

- 721c927: Lazy load twoslasher
- 3372792: Support line numbers in codeblock
- Updated dependencies [3372792]
  - fumadocs-ui@15.3.1

## 3.1.2

### Patch Changes

- 81fe2c2: Remove the need for placeholder lines
- Updated dependencies [52b5ad8]
- Updated dependencies [abce713]
  - fumadocs-ui@15.3.0

## 3.1.1

### Patch Changes

- 085e39f: Fix inline code issues
- Updated dependencies [eb18da9]
- Updated dependencies [085e39f]
- Updated dependencies [4d50bcf]
  - fumadocs-ui@15.2.7

## 3.1.0

### Minor Changes

- b49d236: Support `typesCache` option and `fumadocs-twoslash/cache-fs` similar to Vitepress

### Patch Changes

- Updated dependencies [6bc033a]
  - fumadocs-ui@15.0.14

## 3.0.1

### Patch Changes

- 0f59dfc: Update peer deps
- Updated dependencies [7608f4e]
- Updated dependencies [89ff3ae]
- Updated dependencies [16c8944]
  - fumadocs-ui@15.0.13

## 3.0.0

### Major Changes

- a89d6e0: Require Fumadocs v15 & Tailwind CSS v4

### Patch Changes

- Updated dependencies [a89d6e0]
- Updated dependencies [a84f37a]
- Updated dependencies [f2f9c3d]
  - fumadocs-ui@15.0.0

## 2.0.3

### Patch Changes

- b9601fb: Update Shiki
  - fumadocs-ui@14.7.6

## 2.0.2

### Patch Changes

- 9585561: Fix Twoslash popups focus outline
- 4766292: Support React 19
- Updated dependencies [010da9e]
- Updated dependencies [bebb16b]
- Updated dependencies [9585561]
- Updated dependencies [4766292]
  - fumadocs-ui@14.6.0

## 2.0.1

### Patch Changes

- d6d290c: Upgrade Shiki
  - fumadocs-ui@14.1.0

## 2.0.0

### Major Changes

- 9a10262: **Move Twoslash UI components to `fumadocs-twoslash`**

  **why:** Isolate logic from Fumadocs UI

  **migrate:**

  Before:

  ```ts
  import 'fumadocs-ui/twoslash.css';

  import { Popup } from 'fumadocs-ui/twoslash/popup';
  ```

  After:

  ```ts
  import 'fumadocs-twoslash/twoslash.css';

  import { Popup } from 'fumadocs-twoslash/ui';
  ```

  **Tailwind CSS is now required for Twoslash integration.**

### Patch Changes

- be820c4: Bump deps
- Updated dependencies [34cf456]
- Updated dependencies [d9e908e]
- Updated dependencies [f949520]
- Updated dependencies [ad47fd8]
- Updated dependencies [d9e908e]
- Updated dependencies [367f4c3]
- Updated dependencies [87063eb]
- Updated dependencies [64f0653]
- Updated dependencies [e1ee822]
- Updated dependencies [d9e908e]
- Updated dependencies [d9e908e]
- Updated dependencies [e612f2a]
- Updated dependencies [3d0369a]
- Updated dependencies [9a10262]
- Updated dependencies [d9e908e]
- Updated dependencies [3d054a8]
- Updated dependencies [d9e908e]
- Updated dependencies [be820c4]
- Updated dependencies [be53a0e]
  - fumadocs-ui@14.0.0

## 1.1.3

### Patch Changes

- 0c251e5: Bump deps
- Updated dependencies [0c251e5]
- Updated dependencies [0c251e5]
- Updated dependencies [0c251e5]
  - fumadocs-ui@13.4.2

## 1.1.2

### Patch Changes

- 2cc477f: Fix meta field inherited to child code blocks
- Updated dependencies [8f5b19e]
- Updated dependencies [32ca37a]
- Updated dependencies [9aae448]
- Updated dependencies [c542561]
  - fumadocs-ui@13.3.0

## 1.1.1

### Patch Changes

- 6ed95ea: Fix compatibility issues with Fumadocs UI v13
- Updated dependencies [89190ae]
- Updated dependencies [b02eebf]
- Updated dependencies [f868018]
- Updated dependencies [8aebeab]
- Updated dependencies [c684c00]
- Updated dependencies [8aebeab]
- Updated dependencies [0377bb4]
- Updated dependencies [e8e6a17]
- Updated dependencies [c8964d3]
- Updated dependencies [c901e6b]
- Updated dependencies [daa7d3c]
- Updated dependencies [89190ae]
- Updated dependencies [b02eebf]
- Updated dependencies [4373231]
  - fumadocs-ui@13.0.0

## 1.1.0

### Minor Changes

- 5f86faa: Improve multi-line code blocks

## 1.0.3

### Patch Changes

- 8ef2b68: Bump deps

## 1.0.2

### Patch Changes

- 08e4904: Update types

## 1.0.1

### Patch Changes

- c71b7e3: Ignore injected elements when copying code
`````

## File: packages/twoslash/README.md
`````markdown
# Fumadocs Twoslash

Use Typescript Twolash in Fumadocs.
`````

## File: packages/typescript/test/fixtures/test.mdx
`````
<auto-type-table path="./test-2.ts" name="Player" />
`````

## File: packages/typescript/CHANGELOG.md
`````markdown
# fumadocs-typescript

## 4.0.6

### Patch Changes

- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos

## 4.0.5

### Patch Changes

- a6c909b: Removed unused devDependencies and migrated from `fast-glob` to `tinyglobby`

## 4.0.4

### Patch Changes

- 6b04eed: Fix errors on special keys
- a1f3273: Lazy load compiler instance

## 4.0.3

### Patch Changes

- 3a5595a: Support deprecated properties in Type Table

## 4.0.2

### Patch Changes

- 38117c1: add `null | undefined` to optional props in a object type

## 4.0.1

### Patch Changes

- f67d20f: Fix `remark-auto-type-table` doesn't render `required` property

## 4.0.0

### Major Changes

- b83d946: **Use `createGenerator` API**

  Create a generator instance:

  ```ts
  import { createGenerator } from 'fumadocs-typescript';

  const generator = createGenerator(tsconfig);
  ```

  Refactor:

  ```tsx
  import { remarkAutoTypeTable, createTypeTable } from 'fumadocs-typescript';

  generateDocumentation('./file.ts', 'MyClass', fs.readFileSync('./file.ts').toString())
  generateMDX('content', {...})
  generateFiles({...})
  const processor = createProcessor({
      remarkPlugins: [remarkAutoTypeTable],
  });

  const AutoTypeTable = createTypeTable()
  return <AutoTypeTable {...props} />
  ```

  To:

  ```tsx
  import { AutoTypeTable, remarkAutoTypeTable } from "fumadocs-typescript";

  generator.generateDocumentation({path: './file.ts'}, 'MyClass')
  generateMDX(generator, 'content', { ... })
  generateFiles(generator, { ... })
  const processor = createProcessor({
      remarkPlugins: [
          [remarkAutoTypeTable, { generator }],
      ],
  });

  return <AutoTypeTable generator={generator} {...props} />
  ```

  This ensure the compiler instance is always re-used.

## 3.1.0

### Minor Changes

- 42d68a6: Support `remarkAutoTypeTable` plugin, deprecate MDX generator in favour of new remark plugin

### Patch Changes

- 5d0dd11: Support overriding `renderMarkdown` function

## 3.0.4

### Patch Changes

- 7608f4e: Support showing optional properties on TypeTable

## 3.0.3

### Patch Changes

- b9601fb: Update Shiki

## 3.0.2

### Patch Changes

- c042eb7: Fix private class members

## 3.0.1

### Patch Changes

- d6d290c: Upgrade Shiki

## 3.0.0

### Major Changes

- f9adba6: Return an array of doc entry in `generateDocumentation`

### Minor Changes

- f9adba6: Support inline type syntax in `AutoTypeTable` `type` prop
- f9adba6: Support `createTypeTable` for shared project instance

### Patch Changes

- be820c4: Bump deps

## 2.1.0

### Minor Changes

- 3a2c837: Disable cache on program-level

### Patch Changes

- 0c251e5: Bump deps

## 2.0.1

### Patch Changes

- 8ef2b68: Bump deps

## 2.0.0

### Major Changes

- f75287d: **Introduce `fumadocs-docgen` package.**

  Offer a better authoring experience for advanced use cases.

  - Move `remark-dynamic-content` and `remark-install` plugins to the new package `fumadocs-docgen`.
  - Support Typescript generator by default

  **Usage**

  Add the `remarkDocGen` plugin to your remark plugins.

  ```ts
  import { remarkDocGen, fileGenerator } from 'fumadocs-docgen';

  remark().use(remarkDocGen, { generators: [fileGenerator()] });
  ```

  Generate docs with code blocks.

  ````mdx
  ```json doc-gen:<generator>
  {
    // options
  }
  ```
  ````

  **Migrate**

  For `remarkDynamicContent`, enable `fileGenerator` and use this syntax:

  ````mdx
  ```json doc-gen:file
  {
    "file": "./path/to/my-file.txt"
  }
  ```
  ````

  For `remarkInstall`, it remains the same:

  ```ts
  import { remarkInstall } from 'fumadocs-docgen';
  ```

## 1.0.2

### Patch Changes

- 77b5b70: Fix compatibility problems with Typescript 5.4.3

## 1.0.1

### Patch Changes

- f4aa6b6: Ignore fields marked with `@internal` tag

## 1.0.0

### Major Changes

- 321d1e1f: Support markdown in type description

### Minor Changes

- 722c2d6e: Support generating MDX files
`````

## File: packages/typescript/README.md
`````markdown
# Fumadocs Typescript

Typescript Integration for Fumadocs.
`````

## File: packages/ui/CHANGELOG.md
`````markdown
# next-docs-ui

## 15.6.5

### Patch Changes

- Updated dependencies [658fa96]
  - fumadocs-core@15.6.5

## 15.6.4

### Patch Changes

- dca17d7: Improve search dialog consistency
  - fumadocs-core@15.6.4

## 15.6.3

### Patch Changes

- a2d7940: Fix layout: remove reserved sidebar space when sidebar is disabled in DocsLayout
  - fumadocs-core@15.6.3

## 15.6.2

### Patch Changes

- 1e50889: Fix mobile sidebar trigger visibility when sidebar is disabled
- 353c139: Callout add fallback icons
- 5844c6f: no longer sort type table properties by default
  - fumadocs-core@15.6.2

## 15.6.1

### Patch Changes

- Updated dependencies [1a902ff]
  - fumadocs-core@15.6.1

## 15.6.0

### Minor Changes

- f8d1709: **Redesigned Codeblock Tabs**

  Instead of relying on `Tabs` component, it supports a dedicated tabs component for codeblocks:

  ```tsx
  <CodeBlockTabs>
    <CodeBlockTabsList>
      <CodeBlockTabsTrigger value="value">Name</CodeBlockTabsTrigger>
    </CodeBlockTabsList>
    <CodeBlockTab value="value" asChild>
      <CodeBlock>...</CodeBlock>
    </CodeBlockTab>
  </CodeBlockTabs>
  ```

  The old usage is not deprecated, you can still use them while Fumadocs' remark plugins will generate codeblock tabs using the new way.

### Patch Changes

- bf15617: Fix Notebook layout minor UI inconsistency
- Updated dependencies [d0f8a15]
- Updated dependencies [84918b8]
- Updated dependencies [f8d1709]
  - fumadocs-core@15.6.0

## 15.5.5

### Patch Changes

- e9b1c9c: Support `rainbowColors` API in `<Banner />` component
- d5c9b11: Fix Notebook Layout tab mode `navbar` cannot handle nested tabs
- Updated dependencies [0d3f76b]
  - fumadocs-core@15.5.5

## 15.5.4

### Patch Changes

- 4a1d3cf: Reduce sidebar intensity
- 58b7596: Fix copying line breaks with Twoslash codeblocks
- Updated dependencies [35c3c0b]
  - fumadocs-core@15.5.4

## 15.5.3

### Patch Changes

- Updated dependencies [7d1ac21]
  - fumadocs-core@15.5.3

## 15.5.2

### Patch Changes

- b675728: Redesign search dialog style
- 1b7bc4b: Add `@types/react` to optional peer dependency to avoid version conflict in monorepos
- 82fc4c8: Avoid direct update to passed props.
- Updated dependencies [7a45921]
- Updated dependencies [1b7bc4b]
  - fumadocs-core@15.5.2

## 15.5.1

### Patch Changes

- b4916d2: Move `hide-if-empty` component to Fumadocs Core
- 68526ea: Redesign `fumadocs-ui/components/dialog/search` usage to make it composable, and mark it as stable API.
- Updated dependencies [b4916d2]
- Updated dependencies [8738b9c]
- Updated dependencies [a66886b]
  - fumadocs-core@15.5.1

## 15.5.0

### Minor Changes

- 589d101: **Move TOC closer to page body on larger viewports**

  Changed layout positioning, all layout components now use `fixed` position.

  This may impact sites that:
  - using custom styling on Fumadocs layouts.
  - added a custom footer (see below).

  For custom footer, make sure to add them into `<DocsLayout />` instead:

  ```tsx
  <DocsLayout>
    {children}
    <div className="h-[400px] bg-fd-secondary">Hello World</div>
  </DocsLayout>
  ```

### Patch Changes

- 50f8f7f: Update Home Layout navbar design
- 697d5b4: Support specifying a custom `value` for `Accordion`
  - fumadocs-core@15.5.0

## 15.4.2

### Patch Changes

- Updated dependencies [0ab6c7f]
  - fumadocs-core@15.4.2

## 15.4.1

### Patch Changes

- e72b7b4: hotfix: production source map being ignored
  - fumadocs-core@15.4.1

## 15.4.0

### Minor Changes

- 961b67e: **Bump algolia search to v5**

  This also introduced changes to some APIs since `algoliasearch` v4 and v5 has many differences.

  Now we highly recommend to pass an index name to `sync()`:

  ```ts
  import { algoliasearch } from 'algoliasearch';
  import { sync } from 'fumadocs-core/search/algolia';
  const client = algoliasearch('id', 'key');

  void sync(client, {
    indexName: 'document',
    documents: records,
  });
  ```

  For search client, pass them to `searchOptions`:

  ```tsx
  'use client';

  import { liteClient } from 'algoliasearch/lite';
  import type { SharedProps } from 'fumadocs-ui/components/dialog/search';
  import SearchDialog from 'fumadocs-ui/components/dialog/search-algolia';

  const client = liteClient(appId, apiKey);

  export default function CustomSearchDialog(props: SharedProps) {
    return (
      <SearchDialog
        searchOptions={{
          client,
          indexName: 'document',
        }}
        {...props}
        showAlgolia
      />
    );
  }
  ```

### Patch Changes

- 092fd04: Fallback to `dangerouslySetInnerHTML` for inlined scripts for backward compatibility
- 7d78bc5: Improve `createRelativeLink` and `getPageByHref` for i18n usage
- Updated dependencies [1b999eb]
- Updated dependencies [961b67e]
- Updated dependencies [7d78bc5]
  - fumadocs-core@15.4.0

## 15.3.4

### Patch Changes

- e0c2a92: Improve UI consistency
- 71fc1a5: Mount all children of tabs by default
  - fumadocs-core@15.3.4

## 15.3.3

### Patch Changes

- 05b3bd9: [Internal] require `TagsListItem` to be used with `TagsList`
- 39bf088: Support usage with `Tabs` in primitive way
- e955a98: Hotfix problems with `HideIfEmpty`
- Updated dependencies [4ae7b4a]
  - fumadocs-core@15.3.3

## 15.3.2

### Patch Changes

- 1753cf1: Fix navbar external items and nav menu scroll
- 9b38baf: add `success` type to callout
- 8e862e5: Use native scroll bar for codeblocks and some elements for better performance
- ac0ab12: Improve performance by reducing usage of `@radix-ui/react-scroll-area`
- c25d678: Support Shiki focus notation transformer by default
- Updated dependencies [c25d678]
  - fumadocs-core@15.3.2

## 15.3.1

### Patch Changes

- 3372792: Support line numbers in codeblock
- Updated dependencies [3372792]
  - fumadocs-core@15.3.1

## 15.3.0

### Minor Changes

- 52b5ad8: **Redesign mobile sidebar**

  Mobile sidebar is now a separate component from the desktop one, with its own id `nd-sidebar-mobile`.

  note to advanced use cases: Fumadocs UI now stopped using `fumadocs-core/sidebar`, avoid using the primitive directly as provider is not used.

### Patch Changes

- abce713: Adjust design (Accordion, Tabs, border color of themes)
- Updated dependencies [c05dc03]
  - fumadocs-core@15.3.0

## 15.2.15

### Patch Changes

- 50db874: Remove placeholder space for codeblocks
- Updated dependencies [50db874]
- Updated dependencies [79e75c3]
  - fumadocs-core@15.2.15

## 15.2.14

### Patch Changes

- Updated dependencies [6ea1718]
  - fumadocs-core@15.2.14

## 15.2.13

### Patch Changes

- b433d93: Recommend using custom button/link instead for edit on GitHub button
- 1e07ed8: Support disabling codeblock styles with `.not-fumadocs-codeblock`
  - fumadocs-core@15.2.13

## 15.2.12

### Patch Changes

- b68bb51: Fix sidebar legacy behaviours
- 127e681: Fix Notebook layout ignores `themeSwitch` and `sidebar.collapsible` on nav mode
- Updated dependencies [acff667]
  - fumadocs-core@15.2.12

## 15.2.11

### Patch Changes

- d4d1ba7: Fix sidebar collapsible control search button still visible with search disabled
- 4e62b41: Bundle `lucide-react` as part of library
- 07cd690: Support separators without name
- Updated dependencies [07cd690]
  - fumadocs-core@15.2.11

## 15.2.10

### Patch Changes

- 3a5595a: Support deprecated properties in Type Table
- 8c9fc1f: Fix callout margin
  - fumadocs-core@15.2.10

## 15.2.9

### Patch Changes

- e72af4b: Improve layout
- ea0f468: Fix relative file href with hash
- 7f3c30e: Add `shadcn.css` preset
  - fumadocs-core@15.2.9

## 15.2.8

### Patch Changes

- 4fad539: fix TOC relative position
- a673ef4: Make `@source` in `global.css` optional
  - fumadocs-core@15.2.8

## 15.2.7

### Patch Changes

- eb18da9: Support `searchToggle` option to customise search toggle
- 085e39f: Fix inline code issues
- 4d50bcf: fix banner overlapping with collapsible control
- Updated dependencies [ec85a6c]
- Updated dependencies [e1a61bf]
  - fumadocs-core@15.2.7

## 15.2.6

### Patch Changes

- b07e98c: Deprecate `DocsCategory`, see https://fumadocs.vercel.app/docs/ui/markdown#further-reading-section
- Updated dependencies [d49f9ae]
- Updated dependencies [b07e98c]
- Updated dependencies [3a4bd88]
  - fumadocs-core@15.2.6

## 15.2.5

### Patch Changes

- Updated dependencies [c66ed79]
  - fumadocs-core@15.2.5

## 15.2.4

### Patch Changes

- 1057957: Fix type problems on dynamic codeblock
- Updated dependencies [1057957]
  - fumadocs-core@15.2.4

## 15.2.3

### Patch Changes

- 5e4e9ec: Deprecate I18nProvider in favour of `<RootProvider />` `i18n` prop
- 293178f: revert framework migration on i18n provider
  - fumadocs-core@15.2.3

## 15.2.2

### Patch Changes

- 0829544: Remove unused registry files from dist
- Updated dependencies [0829544]
  - fumadocs-core@15.2.2

## 15.2.1

### Patch Changes

- 22aeafb: Improve Tree context performance
  - fumadocs-core@15.2.1

## 15.2.0

### Patch Changes

- c5af09f: UI: Use `text.previousPage` for previous page navigation
- Updated dependencies [2fd325c]
- Updated dependencies [a7cf4fa]
  - fumadocs-core@15.2.0

## 15.1.3

### Patch Changes

- Updated dependencies [b734f92]
  - fumadocs-core@15.1.3

## 15.1.2

### Patch Changes

- 44d5acf: Improve sidebar UI
- Updated dependencies [3f580c4]
  - fumadocs-core@15.1.2

## 15.1.1

### Patch Changes

- Updated dependencies [c5add28]
- Updated dependencies [f3cde4f]
- Updated dependencies [7c8a690]
- Updated dependencies [b812457]
  - fumadocs-core@15.1.1

## 15.1.0

### Patch Changes

- Updated dependencies [f491f6f]
- Updated dependencies [f491f6f]
- Updated dependencies [f491f6f]
  - fumadocs-core@15.1.0

## 15.0.18

### Patch Changes

- e7e2a2a: Support `createRelativeLink` component factory for using relative file paths in `href`
  - fumadocs-core@15.0.18

## 15.0.17

### Patch Changes

- b790699: Support `themeSwitch` option in layouts to customise theme switch
- Updated dependencies [72f79cf]
  - fumadocs-core@15.0.17

## 15.0.16

### Patch Changes

- fumadocs-core@15.0.16

## 15.0.15

### Patch Changes

- 0e5e14d: Use container media queries on Cards
- Updated dependencies [9f6d39a]
- Updated dependencies [2035cb1]
  - fumadocs-core@15.0.15

## 15.0.14

### Patch Changes

- 6bc033a: Display humanized stars number to GitHub info component
- Updated dependencies [37dc0a6]
- Updated dependencies [796cc5e]
- Updated dependencies [2cc0be5]
  - fumadocs-core@15.0.14

## 15.0.13

### Patch Changes

- 7608f4e: Support showing optional properties on TypeTable
- 89ff3ae: Support GithubInfo component
- 16c8944: Fix Tailwind CSS utilities
  - fumadocs-core@15.0.13

## 15.0.12

### Patch Changes

- 3534a10: Move `fumadocs-core` highlighting utils to `fumadocs-core/highlight` and `fumadocs-core/highlight/client`
- ecacb53: Improve performance
- Updated dependencies [3534a10]
- Updated dependencies [93952db]
  - fumadocs-core@15.0.12

## 15.0.11

### Patch Changes

- 886da49: Fix sidebar layout shifts with `defaultOpen` option
- 04e6c6e: Fix Notebook layout paddings
  - fumadocs-core@15.0.11

## 15.0.10

### Patch Changes

- e8a3ab7: Add collapse button back to sidebar on Notebook layout
- Updated dependencies [d95c21f]
  - fumadocs-core@15.0.10

## 15.0.9

### Patch Changes

- fa5b908: Fix React 18 compatibility
  - fumadocs-core@15.0.9

## 15.0.8

### Patch Changes

- 8f5993b: Support custom nav mode and tabs mode on Notebook layout
  - fumadocs-core@15.0.8

## 15.0.7

### Patch Changes

- 5deaf40: Support icons in separators of `meta.json`
- f782c2c: Improve sidebar design
- Updated dependencies [5deaf40]
  - fumadocs-core@15.0.7

## 15.0.6

### Patch Changes

- Updated dependencies [08236e1]
- Updated dependencies [a06af26]
  - fumadocs-core@15.0.6

## 15.0.5

### Patch Changes

- 14b2f95: Improve accessibility
  - fumadocs-core@15.0.5

## 15.0.4

### Patch Changes

- c892bd9: Improve `DocsCategory` cards
- c892bd9: Always show copy button on codeblocks on touch devices
  - fumadocs-core@15.0.4

## 15.0.3

### Patch Changes

- 47171db: UI: fix ocean theme
  - fumadocs-core@15.0.3

## 15.0.2

### Patch Changes

- a8e9e1f: Bump deps
  - fumadocs-core@15.0.2

## 15.0.1

### Patch Changes

- 421166a: Fix border styles
  - fumadocs-core@15.0.1

## 15.0.0

### Major Changes

- a84f37a: **Migrate to Tailwind CSS v4**

  **migrate:**

  Follow https://tailwindcss.com/blog/tailwindcss-v4 for official migrate guide of Tailwind CSS v4.

  Fumadocs UI v15 redesigned the Tailwind CSS config to fully adhere the new config style, no JavaScript and options needed for plugins.
  Add the following to your CSS file:

  ```css
  @import 'tailwindcss';
  @import 'fumadocs-ui/css/neutral.css';
  @import 'fumadocs-ui/css/preset.css';
  /* if you have Twoslash enabled */
  @import 'fumadocs-twoslash/twoslash.css';

  @source '../node_modules/fumadocs-ui/dist/**/*.js';
  /* if you have OpenAPI enabled */
  @source '../node_modules/fumadocs-openapi/dist/**/*.js';
  ```

  The `fumadocs-ui/css/preset.css` import is required, it declares necessary plugins & styles for Fumadocs UI, and `fumadocs-ui/css/neutral.css` defines the color palette of UI.

  Like the previous `preset` option in Tailwind CSS plugin, you can import other color presets like `fumadocs-ui/css/vitepress.css`.

  You should also pay attention to `@source`, the file paths are relative to the CSS file itself. For your project, it might not be `../node_modules/fumadocs-ui/dist/**/*.js`.

### Patch Changes

- a89d6e0: Support Fumadocs v15
- f2f9c3d: Redesign sidebar
- Updated dependencies [5b8cca8]
- Updated dependencies [a763058]
- Updated dependencies [581f4a5]
  - fumadocs-core@15.0.0

## 14.7.7

### Patch Changes

- 4f2538a: Support `children` prop in custom `Folder` component
- 191012a: `DocsCategory` search based on file path when item isn't present in the tree
- fb6b168: No longer rely on search context on search dialog
  - fumadocs-core@14.7.7

## 14.7.6

### Patch Changes

- Updated dependencies [b9601fb]
  - fumadocs-core@14.7.6

## 14.7.5

### Patch Changes

- 5d41bf1: Enable system option for theme toggle on NoteBook layout
- 900eb6c: Prevent shrink on sidebar icons by default
- a959374: Support `fd-*` prefixes to Tailwind CSS utils
- Updated dependencies [777188b]
  - fumadocs-core@14.7.5

## 14.7.4

### Patch Changes

- 26d9ccb: Fix banner preview
- 036f8e1: Disable hover to open navbar menu by default, can be enabled via `nav.enableHoverToOpen`
- Updated dependencies [bb73a72]
- Updated dependencies [69bd4fe]
  - fumadocs-core@14.7.4

## 14.7.3

### Patch Changes

- 041f230: Support trailing slash
- ca1cf19: Support custom `<Banner />` height
- Updated dependencies [041f230]
  - fumadocs-core@14.7.3

## 14.7.2

### Patch Changes

- Updated dependencies [14b280c]
  - fumadocs-core@14.7.2

## 14.7.1

### Patch Changes

- 18b00c1: Fix `hideSearch` option
- Updated dependencies [72dc093]
  - fumadocs-core@14.7.1

## 14.7.0

### Patch Changes

- a557bb4: revert `contain`
- Updated dependencies [97ed36c]
  - fumadocs-core@14.7.0

## 14.6.8

### Patch Changes

- e95be52: Fix i18n toggle
- f3298ea: Add css prefix by default
  - fumadocs-core@14.6.8

## 14.6.7

### Patch Changes

- Updated dependencies [5474343]
  - fumadocs-core@14.6.7

## 14.6.6

### Patch Changes

- 9c930ea: fix runtime error
  - fumadocs-core@14.6.6

## 14.6.5

### Patch Changes

- 969da26: Improve i18n api
- Updated dependencies [969da26]
  - fumadocs-core@14.6.5

## 14.6.4

### Patch Changes

- 67124b1: Improve theme toggle on Notebook layout
- 1810868: Enable `content-visibility` CSS features
- Updated dependencies [b71064a]
  - fumadocs-core@14.6.4

## 14.6.3

### Patch Changes

- abc3677: Allow `className` to be used with `SidebarItem`
  - fumadocs-core@14.6.3

## 14.6.2

### Patch Changes

- 9908922: Add default icon styles (`transformer`) to sidebar tabs
- ece734f: Support custom children of trigger on `InlineTOC` component
- 1a2597a: Expose `--fd-tocnav-height` CSS variable
- Updated dependencies [2357d40]
  - fumadocs-core@14.6.2

## 14.6.1

### Patch Changes

- 9532855: Hide toc popover when no items
  - fumadocs-core@14.6.1

## 14.6.0

### Minor Changes

- 010da9e: Tabs: support usage without `value`
- bebb16b: Support `DynamicCodeBlock` component

### Patch Changes

- 9585561: Fix Twoslash popups focus outline
- 4766292: Support React 19
- Updated dependencies [4dfde6b]
- Updated dependencies [bebb16b]
- Updated dependencies [4766292]
- Updated dependencies [050b326]
  - fumadocs-core@14.6.0

## 14.5.6

### Patch Changes

- b7745f4: Fix references problem of sidebar tabs
- Updated dependencies [9a18c14]
  - fumadocs-core@14.5.6

## 14.5.5

### Patch Changes

- 06f66d8: improve notebook layout for transparent sidebar
- 2d0501f: Fi sidebar icon trigger
  - fumadocs-core@14.5.5

## 14.5.4

### Patch Changes

- 8e2cb31: fix trivial bugs
  - fumadocs-core@14.5.4

## 14.5.3

### Patch Changes

- c5a5ba0: fix sidebar `defaultOpenLevel`
- f34e895: Support `props` in tag items
- 4c82a3d: Hide toc when it has no items and custom banner & footer
- f8e5157: Fix custom `theme` with Typography plugin
- ad00dd3: Support folder groups on sidebar tabs
  - fumadocs-core@14.5.3

## 14.5.2

### Patch Changes

- 072e349: fix initial sidebar level to 0
  - fumadocs-core@14.5.2

## 14.5.1

### Patch Changes

- 6fd480f: Fix old browser compatibility
  - fumadocs-core@14.5.1

## 14.5.0

### Minor Changes

- 66c70ec: **Replace official Tailwind CSS typography plugin**
  - Other variants like `prose-sm` and `prose-gray` are removed, as it's supposed to only provide support for Fumadocs UI typography styles.

- 05d224c: added the updateAnchor option for the Tabs ui component

### Patch Changes

- fumadocs-core@14.5.0

## 14.4.2

### Patch Changes

- 0f1603a: Fix bugs
  - fumadocs-core@14.4.2

## 14.4.1

### Patch Changes

- 07474cb: fix codeblock paddings
- 48a2c15: Control page styles from layouts
  - fumadocs-core@14.4.1

## 14.4.0

### Minor Changes

- 5fd4e2f: Make TOC collapse to a popover on `lg` screen size instead of `md`
- 5fd4e2f: Support better table styles for Typography plugin
- 8a3f5b0: Make `neutral` the default theme of Fumadocs UI

### Patch Changes

- 5145123: Fix sidebar footer issues
- 64defe0: Support `fumadocs-ui/layouts/notebook` layout
  - fumadocs-core@14.4.0

## 14.3.1

### Patch Changes

- e7443d7: Fix development errors
  - fumadocs-core@14.3.1

## 14.3.0

### Minor Changes

- b8a12ed: Move to `tsc` (experimental)

### Patch Changes

- 80655b3: Improve padding of sidebar tabs and expose it to sidebar
  - fumadocs-core@14.3.0

## 14.2.1

### Patch Changes

- 2949da3: Show 'ctrl' for windows in search toggle
- Updated dependencies [ca94bfd]
  - fumadocs-core@14.2.1

## 14.2.0

### Minor Changes

- e248a0f: Support Orama Cloud integration
- 7a5393b: Replace `cmdk` with custom implementation

### Patch Changes

- Updated dependencies [e248a0f]
  - fumadocs-core@14.2.0

## 14.1.1

### Patch Changes

- Updated dependencies [1573d63]
  - fumadocs-core@14.1.1

## 14.1.0

### Patch Changes

- Updated dependencies [b262d99]
- Updated dependencies [d6d290c]
- Updated dependencies [4a643ff]
- Updated dependencies [b262d99]
- Updated dependencies [90725c1]
  - fumadocs-core@14.1.0

## 14.0.2

### Patch Changes

- bfc2bf2: Fix navbar issues
  - fumadocs-core@14.0.2

## 14.0.1

### Patch Changes

- 1a7d78a: Pass props to replaced layout components via Radix UI `<Slot />`
  - fumadocs-core@14.0.1

## 14.0.0

### Major Changes

- d9e908e: **Refactor import paths for layouts**

  **migrate:** Use

  ```ts
  import { DocsLayout } from 'fumadocs-ui/layouts/docs';

  import { HomeLayout } from 'fumadocs-ui/layouts/home';

  import { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';
  ```

  Instead of

  ```ts
  import { DocsLayout } from 'fumadocs-ui/layout';

  import { HomeLayout } from 'fumadocs-ui/home-layout';

  import { HomeLayoutProps } from 'fumadocs-ui/home-layout';
  ```

- 9a10262: **Move Twoslash UI components to `fumadocs-twoslash`**

  **why:** Isolate logic from Fumadocs UI

  **migrate:**

  Before:

  ```ts
  import 'fumadocs-ui/twoslash.css';

  import { Popup } from 'fumadocs-ui/twoslash/popup';
  ```

  After:

  ```ts
  import 'fumadocs-twoslash/twoslash.css';

  import { Popup } from 'fumadocs-twoslash/ui';
  ```

  **Tailwind CSS is now required for Twoslash integration.**

- d9e908e: **Remove `getImageMeta` from `fumadocs-ui/og`**

  **migrate:** Use Metadata API from `fumadocs-core/server`

- d9e908e: Replace `fumadocs-core/search/shared` with `fumadocs-core/server`
- be53a0e: **`DocsCategory` now accept `from` prop instead of `pages` prop.**

  **why:** This allows sharing the order of items with page tree.
  **migrate:**

  The component now takes `from` prop which is the Source API object.

  ```tsx
  import { source } from '@/lib/source';
  import { DocsCategory } from 'fumadocs-ui/page';

  const page = source.getPage(params.slug);

  <DocsCategory page={page} from={source} />;
  ```

### Minor Changes

- 34cf456: Support `disableThemeSwitch` on layouts
- d9e908e: Bundle icons into dist
- ad47fd8: Show i18n language toggle on home layout
- 87063eb: Add root toggle to sidebar automatically
- 64f0653: Introduce `--fd-nav-height` CSS variable for custom navbar
- e1ee822: Support hast nodes in `toc` variable
- 3d054a8: Support linking to a specific tab

### Patch Changes

- f949520: Support Shiki diff transformer
- 367f4c3: Improve Root Toggle component
- d9e908e: Change default URL of title on i18n mode
- d9e908e: Add center to root toggle
- e612f2a: Make compatible with Next.js 15
- 3d0369a: Improve edit on GitHub button
- be820c4: Bump deps
- Updated dependencies [e45bc67]
- Updated dependencies [d9e908e]
- Updated dependencies [d9e908e]
- Updated dependencies [f949520]
- Updated dependencies [9a0b09f]
- Updated dependencies [9a0b09f]
- Updated dependencies [367f4c3]
- Updated dependencies [e1ee822]
- Updated dependencies [e612f2a]
- Updated dependencies [9a0b09f]
- Updated dependencies [d9e908e]
- Updated dependencies [8ef00dc]
- Updated dependencies [979e301]
- Updated dependencies [d9e908e]
- Updated dependencies [979e301]
- Updated dependencies [15781f0]
- Updated dependencies [be820c4]
- Updated dependencies [d9e908e]
  - fumadocs-core@14.0.0

## 13.4.10

### Patch Changes

- 4cb74d5: Expose more props to Image Zoom
- Updated dependencies [6231ad3]
  - fumadocs-core@13.4.10

## 13.4.9

### Patch Changes

- bcf51a6: Improve banner rainbow variant
- Updated dependencies [083f04a]
  - fumadocs-core@13.4.9

## 13.4.8

### Patch Changes

- 5581733: Add center to root toggle
- 1a327cc: Fix props types of Root Toggle
- Updated dependencies [78e59e7]
  - fumadocs-core@13.4.8

## 13.4.7

### Patch Changes

- 6e1923e: Fix ocean present background repeat
- 6e1923e: Introduce `rainbow` variant on Banner component
- Updated dependencies [6e1923e]
  - fumadocs-core@13.4.7

## 13.4.6

### Patch Changes

- b33aff0: Fix typography styles
- afb697e: Fix Next.js 14.2.8 dynamic import problems
- 6bcd263: Fix Banner component z-index
- Updated dependencies [afb697e]
- Updated dependencies [daa66d2]
  - fumadocs-core@13.4.6

## 13.4.5

### Patch Changes

- d46a3f1: Improve search dialog
  - fumadocs-core@13.4.5

## 13.4.4

### Patch Changes

- Updated dependencies [729928e]
  - fumadocs-core@13.4.4

## 13.4.3

### Patch Changes

- fumadocs-core@13.4.3

## 13.4.2

### Patch Changes

- 0c251e5: Bump deps
- 0c251e5: Support Shiki inline code
- 0c251e5: Improve nested list styles
- Updated dependencies [7dabbc1]
- Updated dependencies [0c251e5]
- Updated dependencies [3b56170]
  - fumadocs-core@13.4.2

## 13.4.1

### Patch Changes

- Updated dependencies [95dbba1]
  - fumadocs-core@13.4.1

## 13.4.0

### Minor Changes

- 26f5360: Support built-in OG Image generation

### Patch Changes

- fumadocs-core@13.4.0

## 13.3.3

### Patch Changes

- Updated dependencies [f8cc167]
  - fumadocs-core@13.3.3

## 13.3.2

### Patch Changes

- 17746a6: Support built-in edit on github button
- Updated dependencies [0e0ef8c]
  - fumadocs-core@13.3.2

## 13.3.1

### Patch Changes

- 7258c4b: Fix thumb not rendered on initial render
  - fumadocs-core@13.3.1

## 13.3.0

### Minor Changes

- 8f5b19e: Introduce `DocsTitle`, `DocsDescription` and `DocsCategory` components
- 32ca37a: Support Clerk-style TOC
- 9aae448: Support multiple toc active items
- c542561: Use cookie to store active locale on `always` mode

### Patch Changes

- Updated dependencies [4916f84]
- Updated dependencies [fd46eb6]
- Updated dependencies [fd46eb6]
- Updated dependencies [fd46eb6]
- Updated dependencies [fd46eb6]
- Updated dependencies [9aae448]
- Updated dependencies [c542561]
  - fumadocs-core@13.3.0

## 13.2.2

### Patch Changes

- Updated dependencies [36b771b]
- Updated dependencies [61b91fa]
  - fumadocs-core@13.2.2

## 13.2.1

### Patch Changes

- Updated dependencies [17fa173]
  - fumadocs-core@13.2.1

## 13.2.0

### Minor Changes

- ba588a2: Support custom max width
- ec983a3: Change default value of `defaultOpenLevel` to 0

### Patch Changes

- 96c9dda: Change Heading scroll margins
- 96c9dda: Hide TOC Popover on full mode
- Updated dependencies [96c9dda]
  - fumadocs-core@13.2.0

## 13.1.0

### Minor Changes

- c8910c4: Add default 'max-height' to codeblocks

### Patch Changes

- 61ef42c: Add `vitepress` theme preset
- deae4dd: Improve theme presets
- c8910c4: Fix empty space on search dialog
- 6c42960: Improve TOC design
- Updated dependencies [f280191]
  - fumadocs-core@13.1.0

## 13.0.7

### Patch Changes

- e7c52f2: Fix code styles in headings
- Updated dependencies [37bbfff]
  - fumadocs-core@13.0.7

## 13.0.6

### Patch Changes

- 1622e36: Fix bug breaking Tailwind CSS IntelliSense VSCode Extension
  - fumadocs-core@13.0.6

## 13.0.5

### Patch Changes

- Updated dependencies [2cf65f6]
  - fumadocs-core@13.0.5

## 13.0.4

### Patch Changes

- Updated dependencies [5355391]
  - fumadocs-core@13.0.4

## 13.0.3

### Patch Changes

- Updated dependencies [978342f]
  - fumadocs-core@13.0.3

## 13.0.2

### Patch Changes

- Updated dependencies [4819820]
  - fumadocs-core@13.0.2

## 13.0.1

### Patch Changes

- fumadocs-core@13.0.1

## 13.0.0

### Major Changes

- 89190ae: **Rename `prefix` option on Tailwind CSS Plugin to `cssPrefix`**

  **why:** The previous name was misleading

  **migrate:** Rename the option.

  ```js
  import { createPreset } from 'fumadocs-ui/tailwind-plugin';

  /** @type {import('tailwindcss').Config} */
  export default {
    presets: [
      createPreset({
        cssPrefix: 'fd',
      }),
    ],
  };
  ```

- b02eebf: **Move `keepCodeBlockBackground` option to code block component**

  **why:** Easier to customise code block styles.

  **migrate:**

  Enable `keepBackground` on `<CodeBlock />`, and remove deprecated usage.

  ```tsx
  import { Pre, CodeBlock } from 'fumadocs-ui/components/codeblock';

  <MDX
    components={{
      pre: ({ ref: _ref, ...props }) => (
        <CodeBlock keepBackground {...props}>
          <Pre>{props.children}</Pre>
        </CodeBlock>
      ),
    }}
  />;
  ```

- f868018: **Replace `secondary` link items with `icon` link items**

  **why:** Link items with type `secondary` has been deprecated long time ago.

  **migrate:** Replace type `secondary` with `icon`.

- 8aebeab: **Change usage of I18nProvider**

  **why:** Make possible to load translations lazily

  **migrate:**

  ```tsx
  import { RootProvider } from 'fumadocs-ui/provider';
  import type { ReactNode } from 'react';
  import { I18nProvider } from 'fumadocs-ui/i18n';

  export default function Layout({
    params: { lang },
    children,
  }: {
    params: { lang: string };
    children: ReactNode;
  }) {
    return (
      <html lang={lang}>
        <body>
          <I18nProvider
            locale={lang}
            // options
            locales={[
              {
                name: 'English',
                locale: 'en',
              },
              {
                name: 'Chinese',
                locale: 'cn',
              },
            ]}
            // translations
            translations={
              {
                cn: {
                  toc: '目錄',
                  search: '搜尋文檔',
                  lastUpdate: '最後更新於',
                  searchNoResult: '沒有結果',
                  previousPage: '上一頁',
                  nextPage: '下一頁',
                },
              }[lang]
            }
          >
            <RootProvider>{children}</RootProvider>
          </I18nProvider>
        </body>
      </html>
    );
  }
  ```

- 8aebeab: **Require `locale` prop on I18nProvider**

  **why:** Fix problems related to pathname parsing

  **migrate:** Pass `locale` parameter to the provider

- 0377bb4: **Rename `id` prop on Tabs component to `groupId`**

  **why:** Conflicted with HTML `id` attribute.

  **migrate:** Rename to `groupId`.

- e8e6a17: **Make Tailwind CSS Plugin ESM-only**

  **why:** Tailwind CSS supported ESM and TypeScript configs.

  **migrate:** Use ESM syntax in your Tailwind CSS config.

- c901e6b: **Remove deprecated `fumadocs-ui/components/api` components**

  **why:** The new OpenAPI integration has its own UI implementation.

  **migrate:** Update to latest OpenAPI integration.

- 89190ae: **Add `fd-` prefix to all Fumadocs UI colors, animations and utilities**

  **why:** The added Tailwind CSS colors may conflict with the existing colors of codebases.

  **migrate:** Enable `addGlobalColors` on Tailwind CSS Plugin or add the `fd-` prefix to class names.

  ```js
  import { createPreset } from 'fumadocs-ui/tailwind-plugin';

  /** @type {import('tailwindcss').Config} */
  export default {
    presets: [
      createPreset({
        addGlobalColors: true,
      }),
    ],
  };
  ```

- b02eebf: **Change code block component usage**

  **why:** The previous usage was confusing, some props are passed directly to `pre` while some are not.

  **migrate:**

  Pass all props to `CodeBlock` component.
  This also includes class names, change your custom styles if necessary.

  ```tsx
  import { Pre, CodeBlock } from 'fumadocs-ui/components/codeblock';

  <MDX
    components={{
      // HTML `ref` attribute conflicts with `forwardRef`
      pre: ({ ref: _ref, ...props }) => (
        <CodeBlock {...props}>
          <Pre>{props.children}</Pre>
        </CodeBlock>
      ),
    }}
  />;
  ```

  You can ignore this if you didn't customise the default `pre` element.

- 4373231: **Remove `RollButton` component**

  **why:** `RollButton` was created because there were no "Table Of Contents" on mobile viewports. Now users can use the TOC Popover to switch between headings, `RollButton` is no longer a suitable design for Fumadocs UI.

  **migrate:** Remove usages, you may copy the [last implementation of `RollButton`](https://github.com/fuma-nama/fumadocs/blob/fumadocs-ui%4012.5.6/packages/ui/src/components/roll-button.tsx).

### Minor Changes

- c684c00: Support to disable container style overriding
- c8964d3: Include `Callout` as default MDX component

### Patch Changes

- daa7d3c: Fix empty folder animation problems
- Updated dependencies [09c3103]
- Updated dependencies [c714eaa]
- Updated dependencies [b02eebf]
  - fumadocs-core@13.0.0

## 12.5.6

### Patch Changes

- a332bee: Support `undefined` state of `defaultOpen` in folder nodes
  - fumadocs-core@12.5.6

## 12.5.5

### Patch Changes

- 3519e6c: Fix TOC overflow problems
  - fumadocs-core@12.5.5

## 12.5.4

### Patch Changes

- fccdfdb: Improve TOC Popover design
- Updated dependencies [fccdfdb]
- Updated dependencies [2ffd5ea]
  - fumadocs-core@12.5.4

## 12.5.3

### Patch Changes

- 5d963f4: Support to disable prefetching links on sidebar
  - fumadocs-core@12.5.3

## 12.5.2

### Patch Changes

- a5c34f0: Support specifying the url of root node when breadcrumbs have `includeRoot` enabled
- Updated dependencies [a5c34f0]
  - fumadocs-core@12.5.2

## 12.5.1

### Patch Changes

- c5d20d0: Fix wrong padding
- 3d8f6cf: Add data attributes to certain components to improve CSS targeting
  - fumadocs-core@12.5.1

## 12.5.0

### Minor Changes

- b9fa99d: Support tag filters in search dialog
- a4bcaa7: Rename `Layout` in `fumadocs-ui/layout` to `HomeLayout` in `fumadocs-ui/home-layout`

### Patch Changes

- d1c7405: Optimize performance
- Updated dependencies [b9fa99d]
- Updated dependencies [525925b]
  - fumadocs-core@12.5.0

## 12.4.2

### Patch Changes

- 503e8e9: Improve Object Collaspible
- Updated dependencies [503e8e9]
  - fumadocs-core@12.4.2

## 12.4.1

### Patch Changes

- fumadocs-core@12.4.1

## 12.4.0

### Minor Changes

- eb36761: Replace link item `secondary` type with `icon` (backward compatible)
- eb36761: Support `secondary` property in link items
- eb36761: Support `button` type link item
- eb36761: Support `on` filter in link items

### Patch Changes

- 33ffa99: Improve design details
  - fumadocs-core@12.4.0

## 12.3.6

### Patch Changes

- 4cc5782: Adding secondary custom links
  - fumadocs-core@12.3.6

## 12.3.5

### Patch Changes

- fumadocs-core@12.3.5

## 12.3.4

### Patch Changes

- fbfd050: Improve the default theme
- eefa75d: Reduce the navbar height
  - fumadocs-core@12.3.4

## 12.3.3

### Patch Changes

- 90d51cb: Fix problem with I18n middleware & language toggle
- Updated dependencies [90d51cb]
  - fumadocs-core@12.3.3

## 12.3.2

### Patch Changes

- Updated dependencies [ca7d0f4]
  - fumadocs-core@12.3.2

## 12.3.1

### Patch Changes

- Updated dependencies [cf852f6]
  - fumadocs-core@12.3.1

## 12.3.0

### Patch Changes

- Updated dependencies [ce3c8ad]
- Updated dependencies [ce3c8ad]
  - fumadocs-core@12.3.0

## 12.2.5

### Patch Changes

- 7c23f7e: No longer set a default size for SVG elements in title
  - fumadocs-core@12.2.5

## 12.2.4

### Patch Changes

- ffb9026: Fix `cmdk` upstream dependency problems
  - fumadocs-core@12.2.4

## 12.2.3

### Patch Changes

- b4824fa: Updated `<APIInfo />` component, so method name appears vertically centered.
- e120e0f: Improve `<Banner/>` component
- 3970b55: Support custom type link items
  - fumadocs-core@12.2.3

## 12.2.2

### Patch Changes

- 72c7991: Improve sidebar
  - fumadocs-core@12.2.2

## 12.2.1

### Patch Changes

- c428a60: Revert the height of docs navbar to 64px
- 018dbd9: Support `Banner` component
  - fumadocs-core@12.2.1

## 12.2.0

### Minor Changes

- 318eaf9: **Redesign TOC popover:** Make the TOC Popover trigger a part of navbar.
- ea22d04: **Improve dynamic sidebar:** Improve animation & close delay

### Patch Changes

- 2f2d9cf: **Improve footer:** Use card-style buttons to match the other buttons
- bcc9f91: Added a new colors for API info badge, so POST, PATCH requests are different from PUT.
- 2f2d9cf: Improve OpenAPI styles
- Updated dependencies [b70ff06]
  - fumadocs-core@12.2.0

## 12.1.3

### Patch Changes

- 2a5db91: Add timeout for hovering after collapsed the sidebar
- 3e98d7d: Support `full` mode on pages
- d06c92a: Support `transparentMode` on secondary (docs) navbar
- 3bdc786: Support Fumadocs OpenAPI 3.1.0
- d06c92a: Fix hot keys order
  - fumadocs-core@12.1.3

## 12.1.2

### Patch Changes

- 284a571: Support Fumadocs OpenAPI v3
- Updated dependencies [b4856d1]
  - fumadocs-core@12.1.2

## 12.1.1

### Patch Changes

- 1c3a127: Redesign Tabs component
- Updated dependencies [a39dbcb]
  - fumadocs-core@12.1.1

## 12.1.0

### Minor Changes

- 0a377a9: **Pass the `icon` prop to code blocks as HTML instead of MDX attribute.**

  **why:** Only MDX flow elements support attributes with JSX value, like:

  ```mdx
  <Pre icon={<svg />}>...</Pre>
  ```

  As Shiki outputs hast elements, we have to convert the output of Shiki to a MDX flow element so that we can pass the `icon` property.

  Now, `rehype-code` passes a HTML string instead of JSX, and render it with `dangerouslySetInnerHTML`:

  ```mdx
  <Pre icon="<svg />">...</Pre>
  ```

  **migrate:** Not needed, it should work seamlessly.

### Patch Changes

- 0a377a9: Close sidebar on collapse
- 5f86faa: Improve multi-line code blocks
- Updated dependencies [0a377a9]
- Updated dependencies [0a377a9]
  - fumadocs-core@12.1.0

## 12.0.7

### Patch Changes

- 51441d3: Fix `RollButton` component problems on Safari
  - fumadocs-core@12.0.7

## 12.0.6

### Patch Changes

- 056bad5: Improve default values
- Updated dependencies [7a29b79]
- Updated dependencies [b0c1242]
  - fumadocs-core@12.0.6

## 12.0.5

### Patch Changes

- 4455d58: Fix `bannerProps` being ignored
  - fumadocs-core@12.0.5

## 12.0.4

### Patch Changes

- 70666d8: Hide file name on breadcrumbs
- f96da27: Improve design details
- 51ca944: Support including separators in breadcrumbs
- Updated dependencies [72dbaf1]
- Updated dependencies [51ca944]
  - fumadocs-core@12.0.4

## 12.0.3

### Patch Changes

- 18928af: Improve mobile experience on Safari
- Updated dependencies [053609d]
  - fumadocs-core@12.0.3

## 12.0.2

### Patch Changes

- Show TOC on mobile devices
  - fumadocs-core@12.0.2

## 12.0.1

### Patch Changes

- 21fe244: Redesign roll button
- 547a61a: Use Menu for link items
  - fumadocs-core@12.0.1

## 12.0.0

### Major Changes

- 62b5abb: **New Layout**
  - Remove navbar from docs layout, replace it with sidebar.
  - On smaller devices, navbar is always shown.
  - Remove exports of internal components, copying components from the repository is now the preferred way.

  **migrate:** On layouts, Rename `nav.githubUrl` to `githubUrl`.
  Modify your stylesheet if necessary.

- 5741224: **Remove deprecated option `enableThemeProvider` from Root Provider**

  **migrate:** Use `theme.enabled` instead.

- 2f8b168: **Replace `<LanguageSelect />` component with `<LanguageToggle />`**

  **migrate:**

  Remove your `<LanguageSelect />` component from the layout. Enable the new language toggle with:

  ```tsx
  import { DocsLayout } from 'fumadocs-ui/layout';

  export default function Layout({ children }: { children: React.ReactNode }) {
    return <DocsLayout i18n>{children}</DocsLayout>;
  }
  ```

### Minor Changes

- d88dfa6: Support switching between page trees with `RootToggle` component

### Patch Changes

- c110040: Fix problems with twoslash codeblocks
- 13a60b9: Heading support typography styles
- 1fe0812: Support translation for theme label
- Updated dependencies [98430e9]
- Updated dependencies [d88dfa6]
- Updated dependencies [ba20694]
- Updated dependencies [57eb762]
  - fumadocs-core@12.0.0

## 11.3.2

### Patch Changes

- 1b8e12b: Use `display: grid` for codeblocks
- Updated dependencies [1b8e12b]
  - fumadocs-core@11.3.2

## 11.3.1

### Patch Changes

- 10ab3e9: Fix sidebar opened by default
  - fumadocs-core@11.3.1

## 11.3.0

### Minor Changes

- 917d87f: Rename sidebar primitive `minWidth` prop to `blockScrollingWidth`

### Patch Changes

- 2a1211e: Support customising search dialog hotkeys
- 9de31e6: Support `withArticle` for MDX Pages
- Updated dependencies [917d87f]
  - fumadocs-core@11.3.0

## 11.2.2

### Patch Changes

- dd0feb2: Support customising sidebar background with opacity
- 72096c3: Support customising theme options from root provider
  - fumadocs-core@11.2.2

## 11.2.1

### Patch Changes

- 8074920: Fix sidebar background width on dynamic sidebar
  - fumadocs-core@11.2.1

## 11.2.0

### Minor Changes

- 3292df1: Support sliding dynamic sidebar

### Patch Changes

- fumadocs-core@11.2.0

## 11.1.3

### Patch Changes

- 2b95c89: Fix codeblock select highlight problems
- cdc52ad: Improve page footer mobile responsibility
- Updated dependencies [88008b1]
- Updated dependencies [944541a]
- Updated dependencies [07a9312]
  - fumadocs-core@11.1.3

## 11.1.2

### Patch Changes

- 58adab1: Improve theme & styles
- ae88793: Improve page footer design
  - fumadocs-core@11.1.2

## 11.1.1

### Patch Changes

- 771314c: Use `sessionStorage` for non-persistent tabs
- 8ef2b68: Bump deps
- fa78241: Fix accordion text alignment
- Updated dependencies [8ef2b68]
- Updated dependencies [26f464d]
- Updated dependencies [26f464d]
  - fumadocs-core@11.1.1

## 11.1.0

### Minor Changes

- 02a014f: Support custom menu items in navbar

### Patch Changes

- fumadocs-core@11.1.0

## 11.0.8

### Patch Changes

- Updated dependencies [98258b5]
  - fumadocs-core@11.0.8

## 11.0.7

### Patch Changes

- Updated dependencies [f7c2c5c]
  - fumadocs-core@11.0.7

## 11.0.6

### Patch Changes

- 8e0ef4b: Support disable search functionality including shortcuts
- Updated dependencies [5653d5d]
- Updated dependencies [5653d5d]
  - fumadocs-core@11.0.6

## 11.0.5

### Patch Changes

- c8ea344: Support disabling search bar
  - fumadocs-core@11.0.5

## 11.0.4

### Patch Changes

- 7b61b2f: Migrate `fumadocs-ui` to fully ESM, adding support for ESM `tailwind.config` file
- Updated dependencies [7b61b2f]
  - fumadocs-core@11.0.4

## 11.0.3

### Patch Changes

- c11e6ce: New color preset: `catppuccin`
  - fumadocs-core@11.0.3

## 11.0.2

### Patch Changes

- 6470d6d: Fix collapse button on smaller viewports
  - fumadocs-core@11.0.2

## 11.0.1

### Patch Changes

- 1136e02: Support modifying css with color presets
- 1136e02: New color preset `neutral`
- f6b4797: Improve Sidebar footer
  - fumadocs-core@11.0.1

## 11.0.0

### Major Changes

- 2d8df75: Replace `nav.links` option with secondary links

  why: A more straightforward API design

  migrate:

  ```diff
  <DocsLayout
  +  links={[
  +    {
  +      type: 'secondary',
  +      text: 'Github',
  +      url: 'https://github.com',
  +      icon: <GithubIcon />,
  +      external: true,
  +    },
  +  ]}
  -  nav={{
  -    links: [
  -      {
  -        icon: <GithubIcon />,
  -        href: 'https://github.com',
  -        label: 'Github',
  -        external: true,
  -      },
  -    ],
  -  }}
  >
    {children}
  </DocsLayout>
  ```

### Patch Changes

- Updated dependencies [2d8df75]
- Updated dependencies [92cb12f]
- Updated dependencies [f75287d]
- Updated dependencies [2d8df75]
  - fumadocs-core@11.0.0

## 10.1.3

### Patch Changes

- 6ace206: Support opening Twoslash popup on mobile
- d0288d1: New theme dusk
- Updated dependencies [bbad52f]
  - fumadocs-core@10.1.3

## 10.1.2

### Patch Changes

- 0facc07: Replace navbar links with secondary links
- fd38022: Improve sidebar collapse
  - fumadocs-core@10.1.2

## 10.1.1

### Patch Changes

- 38d6f22: Improve RTL Layout experience
- Updated dependencies [779c599]
- Updated dependencies [0c01300]
- Updated dependencies [779c599]
  - fumadocs-core@10.1.1

## 10.1.0

### Minor Changes

- 566539a: Support RTL layout

### Patch Changes

- fumadocs-core@10.1.0

## 10.0.5

### Patch Changes

- Updated dependencies [e47c62f]
  - fumadocs-core@10.0.5

## 10.0.4

### Patch Changes

- fumadocs-core@10.0.4

## 10.0.3

### Patch Changes

- b27091f: Support passing search dialog `options` from root provider
- Updated dependencies [6f321e5]
  - fumadocs-core@10.0.3

## 10.0.2

### Patch Changes

- 10e099a: Add scrollbar to TOC
- Updated dependencies [10e099a]
  - fumadocs-core@10.0.2

## 10.0.1

### Patch Changes

- 0e78dc8: Support customising search API URL
- Updated dependencies [c9b7763]
- Updated dependencies [0e78dc8]
- Updated dependencies [d8483a8]
  - fumadocs-core@10.0.1

## 10.0.0

### Major Changes

- 321d1e1f: **Move Typescript integrations to `fumadocs-typescript`**

  why: It is now a stable feature

  migrate: Use `fumadocs-typescript` instead.

  ```diff
  - import { AutoTypeTable } from "fumadocs-ui/components/auto-type-table"
  + import { AutoTypeTable } from "fumadocs-typescript/ui"
  ```

### Patch Changes

- de7ed150: Hide external items from navigation footer
- Updated dependencies [b5d16938]
- Updated dependencies [321d1e1f]
  - fumadocs-core@10.0.0

## 9.1.0

### Minor Changes

- ffc76e9d: Support to override sidebar components
- 1c388ca5: Support `defaultOpen` for folder nodes

### Patch Changes

- Updated dependencies [909b0e35]
- Updated dependencies [691f12aa]
- Updated dependencies [1c388ca5]
  - fumadocs-core@9.1.0

## 9.0.0

### Major Changes

- 071898da: **Remove deprecated usage of `Files` component**

  Why: Since `8.3.0`, you should use the `Folder` component instead for folders. For simplicity, the `title` prop has been renamed to `name`.

  Migrate: Replace folders with the `Folder` component. Rename `title` prop to `name`.

  ```diff
  - <Files>
  - <File title="folder">
  - <File title="file.txt" />
  - </File>
  - </Files>

  + <Files>
  + <Folder name="folder">
  + <File name="file.txt" />
  + </Folder>
  + </Files>
  ```

- 2b355907: **Remove controlled usage for Accordion**

  Why: Components in Fumadocs UI should not be used outside of MDX.

  Migrate: Remove `value` and `onValueChange` props.

### Patch Changes

- fumadocs-core@9.0.0

## 8.3.0

### Minor Changes

- b0003d44: Add `purple` theme
- 9bdb49dd: Add `Folder` export to `fumadocs-ui/components/files`
- 99d66d2d: Rename `title` prop to `name` in `File` and `Folder` component

### Patch Changes

- 5e314eee: Deprecate `input` color and `medium` font size from Tailwind CSS preset
- 52d578d0: Set `darkMode` to `class` by default
- 84667d2f: Improve Accordions
  - fumadocs-core@8.3.0

## 8.2.0

### Minor Changes

- 5c24659: Support code block icons

### Patch Changes

- 09bdf63: Separate stylesheet with Image Zoom component
- Updated dependencies [5c24659]
  - fumadocs-core@8.2.0

## 8.1.1

### Patch Changes

- 153ceaf: Fix typo
  - fumadocs-core@8.1.1

## 8.1.0

### Minor Changes

- 0012eba: Support Typescript Twoslash
- bc936c5: Add `AutoTypeTable` server component

### Patch Changes

- 6c5a39a: Rename Git repository to `fumadocs`
- Updated dependencies [6c5a39a]
- Updated dependencies [eb028b4]
- Updated dependencies [054ec60]
  - fumadocs-core@8.1.0

## 8.0.0

### Major Changes

- a2f4819: **Improve internationalized routing**

  `I18nProvider` now handles routing for you.
  Therefore, `locale` and `onChange` is no longer required.

  ```tsx
  <I18nProvider
    translations={{
      cn: {
        name: 'Chinese', // required
        search: 'Translated Content',
      },
    }}
  ></I18nProvider>
  ```

  `LanguageSelect` detects available options from your translations, therefore, the `languages` prop is removed.

- c608ad2: **Remove deprecated `docsUiPlugins`**

  migrate: Use `createPreset` instead

  ```js
  const { createPreset } = require('fumadocs-ui/tailwind-plugin');

  /** @type {import('tailwindcss').Config} */
  module.exports = {
    content: [
      './components/**/*.{ts,tsx}',
      './app/**/*.{ts,tsx}',
      './content/**/*.mdx',
      './node_modules/fumadocs-ui/dist/**/*.js',
    ],
    presets: [createPreset()],
  };
  ```

- 2ea9437: **Change usage of Code Block component**

  The inner `pre` element is now separated from code block container, making it easier to customise.`

  Before:

  ```tsx
  import { CodeBlock, Pre } from 'fumadocs-ui/mdx/pre';

  <Pre title={title} allowCopy {...props} />;
  ```

  After:

  ```tsx
  import { CodeBlock, Pre } from 'fumadocs-ui/components/codeblock';

  <CodeBlock title={title} allowCopy>
    <Pre {...props} />
  </CodeBlock>;
  ```

- ac424ec: **Update import paths of MDX components**

  why: To improve consistency, all MDX components are located in `/components/*` instead.

  migrate:

  ```diff
  - import { Card, Cards } from "fumadocs-ui/mdx/card"
  + import { Card, Cards } from "fumadocs-ui/components/card"

  - import { Heading } from "fumadocs-ui/mdx/heading"
  + import { Heading } from "fumadocs-ui/components/heading"

  - import { Codeblock, Pre } from "fumadocs-ui/mdx/pre"
  + import { Codeblock, Pre } from "fumadocs-ui/components/codeblock"
  ```

- 2b11c20: **Rename to Fumadocs**

  `next-docs-zeta` -> `fumadocs-core`

  `next-docs-ui` -> `fumadocs-ui`

  `next-docs-mdx` -> `fumadocs-mdx`

  `@fuma-docs/openapi` -> `fumadocs-openapi`

  `create-next-docs-app` -> `create-fumadocs-app`

- 60db195: **Remove Nav component export**

  why: Replaced by the DocsLayout and Layout component, it is now an internal component

  migration: Use the Layout component for sharing the navbar across pages

  ```diff
  - import { Nav } from "fumadocs-ui/nav"
  + import { Layout } from "fumadocs-ui/layout"
  ```

### Minor Changes

- 60db195: **Support transparent navbar**

### Patch Changes

- 974e00f: Collapse API example by default
- Updated dependencies [2ea9437]
- Updated dependencies [cdff313]
- Updated dependencies [1a346a1]
- Updated dependencies [2b11c20]
  - fumadocs-core@8.0.0

## 7.1.2

### Patch Changes

- 9204975: Fix search dialog overflow issues
  - next-docs-zeta@7.1.2

## 7.1.1

### Patch Changes

- next-docs-zeta@7.1.1

## 7.1.0

### Minor Changes

- 40e51a4: Support integration with @fuma-docs/openapi
- d2744a4: Remove tailwindcss-animate

### Patch Changes

- c527044: Support preloading Search Dialog
  - next-docs-zeta@7.1.0

## 7.0.0

### Major Changes

- f995ad9: **Page Footer is now a client component**

  This allows the footer component to find items within the current page tree, which fixes the problem where a item from another page tree is appeared.

  Also removed the `url` and `tree` properties from `DocsPage` since we can pass them via React Context API.

  ```diff
  export default async function Page({ params }) {
    return (
      <DocsPage
  -      url={page.url}
  -      tree={pageTree}
      >
        ...
      </DocsPage>
    );
  }
  ```

  The `footer` property in `DocsPage` has also updated, now you can specify or replace the default footer component.

  ```tsx
  <DocsPage footer={{ items: {} }}>...</DocsPage>
  ```

### Minor Changes

- b30d1cd: **Support theme presets**

  Add theme presets for the Tailwind CSS plugin, the default and ocean presets are available now.

  ```js
  const { docsUi, docsUiPlugins } = require('next-docs-ui/tailwind-plugin');

  /** @type {import('tailwindcss').Config} */
  module.exports = {
    plugins: [
      ...docsUiPlugins,
      docsUi({
        preset: 'ocean',
      }),
    ],
  };
  ```

- 9929c5b: **Support multiple page tree roots**

  You can specify a `root` property in `meta.json`, the nearest root folder will be used as the root of page tree instead.

  ```json
  {
    "title": "Hello World",
    "root": true
  }
  ```

### Patch Changes

- Updated dependencies [9929c5b]
- Updated dependencies [9929c5b]
- Updated dependencies [49201be]
- Updated dependencies [338ea98]
- Updated dependencies [4c1334e]
- Updated dependencies [9929c5b]
  - next-docs-zeta@7.0.0

## 6.1.0

### Minor Changes

- 6e0d2e1: **Support `Layout` for non-docs pages (without page tree)**

  Same as Docs Layout but doesn't include a sidebar. It can be used outside of the docs, a page tree is not required.

  ```jsx
  import { Layout } from 'next-docs-ui/layout';

  export default function HomeLayout({ children }) {
    return <Layout>{children}</Layout>;
  }
  ```

  **`nav.items` prop is deprecated**

  It is now replaced by `links`.

- 2a82e9d: **Support linking to accordions**

  You can now specify an `id` for accordion. The accordion will automatically open when the user is navigating to the page with the specified `id` in hash parameter.

  ```mdx
  <Accordions>
  <Accordion title="My Title" id="my-title">

  My Content

  </Accordion>
  </Accordions>
  ```

### Patch Changes

- 65b7f30: Improve search dialog design
- Updated dependencies [f39ae40]
  - next-docs-zeta@6.1.0

## 6.0.2

### Patch Changes

- next-docs-zeta@6.0.2

## 6.0.1

### Patch Changes

- 515a3e1: Fix inline code blocks are not highlighted
  - next-docs-zeta@6.0.1

## 6.0.0

### Major Changes

- 983ede8: **Remove `not-found` component**

  The `not-found` component was initially intended to be the default 404 page. However, we found that the Next.js default one is good enough. For advanced cases, you can always build your own 404 page.

- ebe8d9f: **Support Tailwind CSS plugin usage**

  If you are using Tailwind CSS for your docs, it's now recommended to use the official plugin instead.

  ```js
  const { docsUi, docsUiPlugins } = require('next-docs-ui/tailwind-plugin');

  /** @type {import('tailwindcss').Config} */
  module.exports = {
    darkMode: 'class',
    content: [
      './components/**/*.{ts,tsx}',
      './app/**/*.{ts,tsx}',
      './content/**/*.mdx',
      './node_modules/next-docs-ui/dist/**/*.js',
    ],
    plugins: [...docsUiPlugins, docsUi],
  };
  ```

  The `docsUi` plugin adds necessary utilities & colors, and `docsUiPlugins` are its dependency plugins which should not be missing.

- 7d89e83: **Add required property `url` to `<DocsPage />` component**

  You must pass the URL of current page to `<DocsPage />` component.

  ```diff
  export default function Page({ params }) {
    return (
      <DocsPage
  +      url={page.url}
        toc={page.data.toc}
      >
        ...
      </DocsPage>
    )
  }
  ```

  **`footer` property is now optional**

  Your `footer` property in `<DocsPage />` will be automatically generated if not specified.

  ```ts
  findNeighbour(tree, url);
  ```

- 0599d50: **Separate MDX components**

  Previously, you can only import the code block component from `next-docs-ui/mdx` (Client Component) and `next-docs-ui/mdx-server` (Server Component).

  This may lead to confusion, hence, it is now separated into multiple files. You can import these components regardless it is either a client or a server component.

  Notice that `MDXContent` is now renamed to `DocsBody`, you must import it from `next-docs-ui/page` instead.

  ```diff
  - import { MDXContent } from "next-docs-ui/mdx"
  - import { MDXContent } from "next-docs-ui/mdx-server"

  + import { DocsBody } from "next-docs-ui/page"
  ```

  ```diff
  - import { Card, Cards } from "next-docs-ui/mdx"
  + import { Card, Cards } from "next-docs-ui/mdx/card"

  - import { Pre } from "next-docs-ui/mdx"
  + import { Pre } from "next-docs-ui/mdx/pre"

  - import { Heading } from "next-docs-ui/mdx"
  + import { Heading } from "next-docs-ui/mdx/heading"

  - import defaultComponents from "next-docs-ui/mdx"
  + import defaultComponents from "next-docs-ui/mdx/default-client"

  - import defaultComponents from "next-docs-ui/mdx-server"
  + import defaultComponents from "next-docs-ui/mdx/default"
  ```

### Minor Changes

- 56a35ce: Support custom `searchOptions` in Algolia Search Dialog

### Patch Changes

- 5c98f7f: Support custom attributes to `pre` element inside code blocks
- Updated dependencies [9ef047d]
  - next-docs-zeta@6.0.0

## 5.0.0

### Minor Changes

- de44efe: Migrate to Shikiji
- de44efe: Support code highlighting options

### Patch Changes

- Updated dependencies [de44efe]
- Updated dependencies [de44efe]
  - next-docs-zeta@5.0.0

## 4.0.9

### Patch Changes

- 70545e7: Support `enableThemeProvider` option in RootProvider
- Updated dependencies [a883009]
  - next-docs-zeta@4.0.9

## 4.0.8

### Patch Changes

- e0c5c96: Make ESM only
- Updated dependencies [e0c5c96]
  - next-docs-zeta@4.0.8

## 4.0.7

### Patch Changes

- b9af5ed: Update tsup & dependencies
- Updated dependencies [b9af5ed]
  - next-docs-zeta@4.0.7

## 4.0.6

### Patch Changes

- Updated dependencies [ff38f6e]
  - next-docs-zeta@4.0.6

## 4.0.5

### Patch Changes

- f00e38f: Use `dvh` for sidebar height
  - next-docs-zeta@4.0.5

## 4.0.4

### Patch Changes

- 1b10e13: Default accordion type to "single"
  - next-docs-zeta@4.0.4

## 4.0.3

### Patch Changes

- Updated dependencies [0cc10cb]
  - next-docs-zeta@4.0.3

## 4.0.2

### Patch Changes

- next-docs-zeta@4.0.2

## 4.0.1

### Patch Changes

- 927714a: Remove dropdown from theme toggle
- d58e90a: Use await imports to import client components in Server Components
- cc1fe39: Render TOC header & footer in Server Component
- 01b23e2: Support Next.js 14
- d58e90a: Add y margins to Callout and Pre component
- Updated dependencies [2da93d8]
- Updated dependencies [01b23e2]
  - next-docs-zeta@4.0.1

## 4.0.0

### Minor Changes

- 6c4a782: Improve CommonJS/ESM compatibility

  Since this release, all server utilities will be CommonJS by default unless
  they have referenced ESM modules in the code. For instance,
  `next-docs-zeta/middleware` is now a CommonJS file. However, some modules,
  such as `next-docs-zeta/server` requires ESM-only package, hence, they remain
  a ESM file.

  Notice that the extension of client-side files is now `.js` instead of `.mjs`,
  but they're still ESM.

  **Why?**

  After migrating to `.mjs` Next.js config file, some imports stopped to work.
  The built-in Next.js bundler seems can't resolve these `next` imports in
  external packages, causing errors when modules have imported Next.js itself
  (e.g. `next/image`) in the code.

  By changing client-side files extension to `.mjs` and using CommonJS for
  server-side files, this error is solved.

- 6c4a782: Support Server Component usage for MDX default components

### Patch Changes

- b2112e8: Improve default codeblock
- 6c4a782: Fix sidebar opening issue
- Updated dependencies [6c4a782]
- Updated dependencies [6c4a782]
  - next-docs-zeta@4.0.0

## 4.0.0

### Minor Changes

- 678cd3d: Improve CommonJS/ESM compatibility

  Since this release, all server utilities will be CommonJS by default unless
  they have referenced ESM modules in the code. For instance,
  `next-docs-zeta/middleware` is now a CommonJS file. However, some modules,
  such as `next-docs-zeta/server` requires ESM-only package, hence, they remain
  a ESM file.

  Notice that the extension of client-side files is now `.js` instead of `.mjs`,
  but they're still ESM.

  **Why?**

  After migrating to `.mjs` Next.js config file, some imports stopped to work.
  The built-in Next.js bundler seems can't resolve these `next` imports in
  external packages, causing errors when modules have imported Next.js itself
  (e.g. `next/image`) in the code.

  By changing client-side files extension to `.mjs` and using CommonJS for
  server-side files, this error is solved.

- d2eb490: Support Server Component usage for MDX default components

### Patch Changes

- 0175b4f: Fix sidebar opening issue
- Updated dependencies [678cd3d]
- Updated dependencies [24245a3]
  - next-docs-zeta@4.0.0

## 3.0.0

### Minor Changes

- 522ed48: Update typography & layout styles

### Patch Changes

- a4a8120: Update search utilities import paths.

  Search Utilities in `next-docs-zeta/server` is now moved to
  `next-docs-zeta/search` and `next-docs-zeta/server-algolia`.

  Client-side Changes: `next-docs-zeta/search` -> `next-docs-zeta/search/client`
  `next-docs-zeta/search-algolia` -> `next-docs-zeta/search-algolia/client`

  If you're using Next Docs UI, make sure to import the correct path.

- Updated dependencies [1043532]
- Updated dependencies [7a0690b]
- Updated dependencies [a4a8120]
  - next-docs-zeta@3.0.0

## 2.4.1

### Patch Changes

- dc4f10d: Fix Callout component overflow
- 841a18b: Support passing extra props to Card components
- Updated dependencies [dfc8b44]
- Updated dependencies [ef4d8cc]
  - next-docs-zeta@2.4.1

## 2.4.0

### Minor Changes

- 82c4fc6: Override default typography styles
- 25e6856: Create Callout component

### Patch Changes

- 1cb6385: Improve Inline TOC component
- Updated dependencies [27ce871]
  - next-docs-zeta@2.4.0

## 2.3.3

### Patch Changes

- 634f7d3: Reduce dependencies
- 996a914: Create Inline TOC component
- eac081c: Update github urls & author name
- Updated dependencies [634f7d3]
- Updated dependencies [eac081c]
  - next-docs-zeta@2.3.3

## 2.3.2

### Patch Changes

- e0ebafa: Improve global padding
  - next-docs-zeta@2.3.2

## 2.3.1

### Patch Changes

- cd0b4a3: Support CSS classes usage for steps component
- cd0b4a3: Fix TOC marker position
  - next-docs-zeta@2.3.1

## 2.3.0

### Minor Changes

- 32a4669: Support algolia search dialog

### Patch Changes

- cef6143: Fix toc marker position
- 32a4669: Improve search API usage
- b65219c: Separate default and custom search dialog
- 9c3bc86: Improve i18n language select
- 6664178: Support custom search function for search dialog
- Updated dependencies [6664178]
- Updated dependencies [a0f9911]
- Updated dependencies [6664178]
  - next-docs-zeta@2.3.0

## 2.2.0

### Minor Changes

- 1ff7172: Remove support for importing "next-docs-ui/components", please use
  "next-docs-ui/nav" instead

### Patch Changes

- e546f4e: Hotfix sidebar collapsible not closing
  - next-docs-zeta@2.2.0

## 2.1.2

### Patch Changes

- a3f443f: Improve colors in light mode
- 2153fc8: Improve navbar transparent mode
- 4e7e0d2: Replace `next-docs-ui/components` with `next-docs-ui/nav`
- 4816737: Fix sidebar collapsible button
- Updated dependencies [dfbbc17]
- Updated dependencies [79227d8]
  - next-docs-zeta@2.1.2

## 2.1.1

### Patch Changes

- 14459cf: Fix image-zoom causes viewport overflow on IOS devices
- a015445: Improve search toggle
- 794c2c6: Remove default icon from cards
  - next-docs-zeta@2.1.1

## 2.1.0

### Minor Changes

- db050fc: Redesign default theme & layout

### Patch Changes

- b527988: Files component support custom icons
- 69a4469: Animate TOC marker
- dbe1bcf: Support transparent navbar for custom navbar
- Updated dependencies [a5a661e]
  - next-docs-zeta@2.1.0

## 2.0.3

### Patch Changes

- caa7e98: Fix sidebar animation problems
- caa7e98: Improve copy button in codeblocks
  - next-docs-zeta@2.0.3

## 2.0.2

### Patch Changes

- 74e5e85: Several UI improvements
- Support adding header to TOC component
- Updated dependencies [74e5e85]
- Updated dependencies [72e9fdf]
  - next-docs-zeta@2.0.2

## 2.0.1

### Patch Changes

- 8a05955: Improve syntax highlighting
- Updated dependencies [48c5256]
  - next-docs-zeta@2.0.1

## 2.0.0

### Major Changes

- 9bf1297: Update API usage

### Patch Changes

- e8b3e50: Use react-medium-image-zoom for zoom images
- 6c408d0: Change layout width
  - next-docs-zeta@2.0.0

## 1.6.9

### Patch Changes

- 5ee874c: Create Accordions component
- 1630f74: Add default border to TOC content
  - next-docs-zeta@1.6.9

## 1.6.8

### Patch Changes

- 4cf4552: Fix aria-controls warning & support default index
  - next-docs-zeta@1.6.8

## 1.6.7

### Patch Changes

- f72a4c1: Improve animations & layout
- 88bab2f: Support `lastUpdate` in page
- f1846e8: Support i18n search dialog placeholder
  - next-docs-zeta@1.6.7

## 1.6.6

### Patch Changes

- be8a93d: Support sidebar default open level
  - next-docs-zeta@1.6.6

## 1.6.5

### Patch Changes

- b8a76f8: Fix theme toggle wrong icon
- 7337d59: Create Zoom Image component
- 79abe84: Support collapsible sidebar
- Updated dependencies [79abe84]
  - next-docs-zeta@1.6.5

## 1.6.4

### Patch Changes

- e6ebf6a: Rename `sidebarContent` to `sidebarFooter`
- e01bf3a: Allow `true` to keep default
- e6ebf6a: Imrove sidebar banner
  - next-docs-zeta@1.6.4

## 1.6.3

### Patch Changes

- Support replacing breadcrumb
- 8d07003: Replace type of `TreeNode[]` with `PageTree`
- Updated dependencies [8d07003]
  - next-docs-zeta@1.6.3

## 1.6.2

### Patch Changes

- 5512300: Support custom navbar items
- af8720b: Improve default code block
- 2836799: Support I18n text in built-in components
  - next-docs-zeta@1.6.2

## 1.6.1

### Patch Changes

- 689c75d: Create Files component
- Updated dependencies [fc6279e]
  - next-docs-zeta@1.6.1

## 1.6.0

### Patch Changes

- 037d5e5: Export default mdx components
- Updated dependencies [cdd30d5]
- Updated dependencies [edb9930]
  - next-docs-zeta@1.6.0

## 1.5.3

### Patch Changes

- fa8d4cf: Update dependencies
- f0ab1ba: Improve typography
- Updated dependencies [fa8d4cf]
  - next-docs-zeta@1.5.3

## 1.5.2

### Patch Changes

- 1906e80: Create steps component
  - next-docs-zeta@1.5.2

## 1.5.1

### Patch Changes

- d4f718d: Support disabling TOC & Sidebar
  - next-docs-zeta@1.5.1

## 1.5.0

### Patch Changes

- Updated dependencies [fb2abb3]
  - next-docs-zeta@1.5.0

## 1.4.1

### Patch Changes

- 8883553: Support tabs component
- d084de2: Export default search dialog
- Improve Search Dialog UI
- Updated dependencies
- Updated dependencies [3d92c92]
  - next-docs-zeta@1.4.1

## 1.4.0

### Minor Changes

- 45a174a: Split roll-button into optional component

### Patch Changes

- ed385ab: Add Type Table component
- 5407360: Improve sidebar layout
- Updated dependencies [0f106d9]
  - next-docs-zeta@1.4.0

## 1.3.1

### Patch Changes

- 21725e4: Support replacing default search dialog component
- 7fb2b9e: Support custom page & folder icons
- Updated dependencies [ff05f5d]
- Updated dependencies [7fb2b9e]
  - next-docs-zeta@1.3.1

## 1.3.0

### Minor Changes

- 98226d9: Rewrite slugger and TOC utilities

### Patch Changes

- 6999268: Support custom codeblock meta in Codeblocks
- Change default typography
- Updated dependencies [98226d9]
  - next-docs-zeta@1.3.0

## 1.2.1

### Patch Changes

- 1b626c9: Redesign UI
- ce10df9: Support custom sidebar banner
- Updated dependencies [b15895f]
  - next-docs-zeta@1.2.1

## 1.2.0

### Minor Changes

- Remove `tree` prop from Docs Page, replaced by pages context.

### Patch Changes

- 5f248fb: Support Auto Scroll in TOC for headless docs
- Updated dependencies [5f248fb]
  - next-docs-zeta@1.2.0

## 1.1.4

### Patch Changes

- 496a6b0: Improve footer design
- 496a6b0: Configure eslint + prettier
- Updated dependencies [496a6b0]
  - next-docs-zeta@1.1.4

## 1.1.3

### Patch Changes

- 10d31e6: Fix sidebar scrollbars disappeared
- Updated dependencies [0998b1b]
  - next-docs-zeta@1.1.3

## 1.1.2

### Patch Changes

- Fix aria attributes
- Improve footer styles
- Updated dependencies
  - next-docs-zeta@1.1.2

## 1.1.1

### Patch Changes

- Fix codeblocks not being generated correctly
  - next-docs-zeta@1.1.1

## 1.1.0

### Minor Changes

- 524ca9a: Support page footer

### Patch Changes

- d810bbd: Improve codeblock styles
- d810bbd: Add `<RollButton />` component
- Updated dependencies [255fc92]
  - next-docs-zeta@1.1.0

## 1.0.0

### Minor Changes

- d30d57f: Support optional I18n context provider

### Patch Changes

- Improve codeblock styles
- Updated dependencies [8e4a001]
- Updated dependencies [4fa45c0]
- Updated dependencies [0983891]
  - next-docs-zeta@1.0.0

## 0.3.2

### Patch Changes

- Fix unexpected trailing slash on Contentlayer v0.3.4
- Add Auto scroll for TOC
  - next-docs-zeta@0.3.2

## 0.3.1

### Patch Changes

- Use Radix UI scroll area
- d91de39: Fix sticky position for TOC and Sidebar
  - next-docs-zeta@0.3.1

## 0.3.0

### Minor Changes

- Support next.js images in MDX files

### Patch Changes

- next-docs-zeta@0.3.0

## 0.1.2

### Patch Changes

- 67cd8ab: Remove unused files in dist
- Updated dependencies [67cd8ab]
  - next-docs-zeta@0.2.1

## 0.1.1

### Patch Changes

- Updated dependencies [5ff94af]
- Updated dependencies [5ff94af]
  - next-docs-zeta@0.2.0
`````

## File: packages/ui/README.md
`````markdown
# Fumadocs UI

The Next.js framework for building documentation website.

[Read Documentation](https://fumadocs.vercel.app/docs/ui)
`````

## File: README.md
`````markdown
![banner](./apps/docs/public/banner.png)

The framework for building documentation websites in Next.js.

📘 Learn More: [Documentation](https://fumadocs.vercel.app).

## Compatibility

All packages are **ESM only**.

## Sticker

![logo](./documents/logo.png)

Welcome to print it out :D

## Contributions

Make sure to read the [Contributing Guide](/.github/contributing.md) before submitting a pull request.
`````
