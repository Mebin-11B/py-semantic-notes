---
title: "GitHub - murerkinn/bookshelf: Self-hosted ebook library that runs on object storage - a Cloudflare Worker over R2, or a Node server over a directory. No database. · GitHub"
url: https://github.com/murerkinn/bookshelf
clipped: 2026-08-31 12:26:34
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [GitHub - murerkinn/bookshelf: Self-hosted ebook library that runs on object storage - a Cloudflare Worker over R2, or a Node server over a directory. No database. · GitHub](https://github.com/murerkinn/bookshelf)

## Full Article

[Skip to content](https://github.com/murerkinn/bookshelf#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [murerkinn](https://github.com/murerkinn)    
    /
    
      [bookshelf](https://github.com/murerkinn/bookshelf)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fmurerkinn%2Fbookshelf)    You must be signed in to change notification settings

  

  
- 
          [Fork
    12](https://github.com/login?return_to=%2Fmurerkinn%2Fbookshelf)
  

  
- 
        
        [Star
          340](https://github.com/login?return_to=%2Fmurerkinn%2Fbookshelf)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/murerkinn/bookshelf/branches)[Tags](https://github.com/murerkinn/bookshelf/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[79 Commits](https://github.com/murerkinn/bookshelf/commits/main/)79 Commits

## Folders and files

NameNameLast commit messageLast commit date[.github](https://github.com/murerkinn/bookshelf/tree/main/.github)[.github](https://github.com/murerkinn/bookshelf/tree/main/.github)  [apps/bookshelf](https://github.com/murerkinn/bookshelf/tree/main/apps/bookshelf)[apps/bookshelf](https://github.com/murerkinn/bookshelf/tree/main/apps/bookshelf)  [docker](https://github.com/murerkinn/bookshelf/tree/main/docker)[docker](https://github.com/murerkinn/bookshelf/tree/main/docker)  [docs](https://github.com/murerkinn/bookshelf/tree/main/docs)[docs](https://github.com/murerkinn/bookshelf/tree/main/docs)  [packages](https://github.com/murerkinn/bookshelf/tree/main/packages)[packages](https://github.com/murerkinn/bookshelf/tree/main/packages)  [tools](https://github.com/murerkinn/bookshelf/tree/main/tools)[tools](https://github.com/murerkinn/bookshelf/tree/main/tools)  [.dockerignore](https://github.com/murerkinn/bookshelf/blob/main/.dockerignore)[.dockerignore](https://github.com/murerkinn/bookshelf/blob/main/.dockerignore)  [.gitignore](https://github.com/murerkinn/bookshelf/blob/main/.gitignore)[.gitignore](https://github.com/murerkinn/bookshelf/blob/main/.gitignore)  [.nvmrc](https://github.com/murerkinn/bookshelf/blob/main/.nvmrc)[.nvmrc](https://github.com/murerkinn/bookshelf/blob/main/.nvmrc)  [CLAUDE.md](https://github.com/murerkinn/bookshelf/blob/main/CLAUDE.md)[CLAUDE.md](https://github.com/murerkinn/bookshelf/blob/main/CLAUDE.md)  [CONTRIBUTING.md](https://github.com/murerkinn/bookshelf/blob/main/CONTRIBUTING.md)[CONTRIBUTING.md](https://github.com/murerkinn/bookshelf/blob/main/CONTRIBUTING.md)  [Dockerfile](https://github.com/murerkinn/bookshelf/blob/main/Dockerfile)[Dockerfile](https://github.com/murerkinn/bookshelf/blob/main/Dockerfile)  [LICENSE](https://github.com/murerkinn/bookshelf/blob/main/LICENSE)[LICENSE](https://github.com/murerkinn/bookshelf/blob/main/LICENSE)  [README.md](https://github.com/murerkinn/bookshelf/blob/main/README.md)[README.md](https://github.com/murerkinn/bookshelf/blob/main/README.md)  [SECURITY.md](https://github.com/murerkinn/bookshelf/blob/main/SECURITY.md)[SECURITY.md](https://github.com/murerkinn/bookshelf/blob/main/SECURITY.md)  [THIRD-PARTY-NOTICES.md](https://github.com/murerkinn/bookshelf/blob/main/THIRD-PARTY-NOTICES.md)[THIRD-PARTY-NOTICES.md](https://github.com/murerkinn/bookshelf/blob/main/THIRD-PARTY-NOTICES.md)  [biome.json](https://github.com/murerkinn/bookshelf/blob/main/biome.json)[biome.json](https://github.com/murerkinn/bookshelf/blob/main/biome.json)  [bookshelf.config.json](https://github.com/murerkinn/bookshelf/blob/main/bookshelf.config.json)[bookshelf.config.json](https://github.com/murerkinn/bookshelf/blob/main/bookshelf.config.json)  [compose.yaml](https://github.com/murerkinn/bookshelf/blob/main/compose.yaml)[compose.yaml](https://github.com/murerkinn/bookshelf/blob/main/compose.yaml)  [package-lock.json](https://github.com/murerkinn/bookshelf/blob/main/package-lock.json)[package-lock.json](https://github.com/murerkinn/bookshelf/blob/main/package-lock.json)  [package.json](https://github.com/murerkinn/bookshelf/blob/main/package.json)[package.json](https://github.com/murerkinn/bookshelf/blob/main/package.json)  [turbo.json](https://github.com/murerkinn/bookshelf/blob/main/turbo.json)[turbo.json](https://github.com/murerkinn/bookshelf/blob/main/turbo.json)  View all files

## Repository files navigation

# Bookshelf

A self-hosted library for the ebooks you already own. Put your EPUBs and PDFs in
a folder, publish them, and read them in any browser — or on your Kobo, through
the [OPDS catalog](https://github.com/murerkinn/bookshelf/blob/main/docs/opds.md).

Run it as a Cloudflare Worker over R2, or as a Node server over a directory on
your own machine. Both use the same code and the same library.

📖 [Full documentation](https://murerkinn.github.io/bookshelf/)

## Try it in a minute

You'll need Node 24 or newer and a Unix-like system. Windows isn't supported —
the sync tool looks for its image tools with  `which` .
 `git clone https://github.com/murerkinn/bookshelf.git
cd bookshelf
npm install
npm run demo` 

 `npm run demo`  writes nine generated public-domain books into  `books/`  — eight
EPUBs and a PDF, so both readers are one click away. It downloads nothing. Then
publish and run them by whichever route below.

The checked-in  `bookshelf.config.json`  points at Cloudflare R2, so  `npm run sync`  goes there unless you change it. For a local look, switch it to the
filesystem provider first:
 `// bookshelf.config.json
{ "storage": { "provider": "fs", "directory": "shelf-data" } }` 

## Set up your own

Put your books in  `books/` , then pick where the library should live.

### With Docker

The shortest route, and the image ships the tools that make covers.
 `mkdir books && cp ~/Downloads/*.epub books/
docker compose run --rm sync --create
docker compose up -d` 

Your shelf is on [http://localhost:3000](http://localhost:3000). Sync flags pass through, so
 `docker compose run --rm sync --force`  works as it does locally.

Back up the  `library`  volume — it holds your published books and your reading
positions. To bind-mount a host directory instead, chown it first:
 `chown -R 1000:1000 /srv/bookshelf` 

### On a machine you own

No account anywhere.
 `// bookshelf.config.json
{ "storage": { "provider": "fs", "directory": "shelf-data" } }` 
 `npm run sync -- --create
npm run build
npm start -w @bookshelf/app` 

More in [the filesystem provider](https://github.com/murerkinn/bookshelf/blob/main/docs/providers/fs.md).

### On Cloudflare

You'll need a Cloudflare account. Edit  `bookshelf.config.json`  and
 `apps/bookshelf/wrangler.jsonc`  so they name your bucket and Worker — if they
disagree, the sync tool stops before uploading.
 `npx wrangler login
npm run sync -- --create
npm run deploy` 

More in [the R2 provider](https://github.com/murerkinn/bookshelf/blob/main/docs/providers/r2.md).

## Before you commit a library to it

There is no authentication. Anyone who can reach your shelf can download
every book in it, and pick any profile while doing it. The
[OPDS catalog](https://github.com/murerkinn/bookshelf/blob/main/docs/opds.md) makes it machine-enumerable as well. Put it on a
network you trust, or behind something that asks who's calling.

Nothing is encrypted. Your library is stored in the clear, and object keys
are slugified titles — a listing of your storage names your shelf. With the
filesystem provider you can keep it on
[an encrypted volume](https://github.com/murerkinn/bookshelf/blob/main/docs/providers/fs.md#encrypting-your-library-at-rest)
today.

Two devices reading one profile at once is last-write-wins.

[What's missing](https://github.com/murerkinn/bookshelf/blob/main/docs/roadmap.md) has the full list.

## Configuration

variable
what it does

 `BOOKSHELF_READ_ONLY` 
set to  `1`  and storage keeps serving but stops accepting. Profiles can't be added, renamed or deleted, and reading positions stay in the browser. Set this on anything strangers can reach

 `BOOKSHELF_PROVIDER` 
override the provider the build was made with

 `BOOKSHELF_DIRECTORY` 
override where the filesystem provider looks

 `BOOKSHELF_SITE_URL` 
the public address, for link previews and canonical URLs. Set it behind a proxy that doesn't say so

Everything else lives in  `bookshelf.config.json`  — see
[publishing](https://github.com/murerkinn/bookshelf/blob/main/docs/publishing.md#configure-where-things-go).

## Commands

All from the repository root.
 `npm run dev          # local dev server, against the local R2 bucket
npm run sync         # build the library and publish it
npm run build        # build every workspace
npm run check-types  # typecheck every workspace
npm run preview      # build + run the Worker locally
npm run deploy       # build + deploy to Cloudflare Workers
npm test             # the test suite
npm run lint         # biome, across the repo` 

 `npm run cf-typegen -w @bookshelf/app`  regenerates  `cloudflare-env.d.ts`  after
you edit  `wrangler.jsonc` .

## Documentation

Published at [https://murerkinn.github.io/bookshelf/](https://murerkinn.github.io/bookshelf/).

[Publishing a library](https://github.com/murerkinn/bookshelf/blob/main/docs/publishing.md)
the sync tool, its flags, and covers

[The library format](https://github.com/murerkinn/bookshelf/blob/main/docs/library-format.md)
what ends up in storage, and what to back up

[Storage providers](https://github.com/murerkinn/bookshelf/blob/main/docs/providers/README.md)
choosing where your library lives

[Cloudflare R2](https://github.com/murerkinn/bookshelf/blob/main/docs/providers/r2.md)
setup, deploying, publishing locally

[Filesystem](https://github.com/murerkinn/bookshelf/blob/main/docs/providers/fs.md)
your own machine or a VPS

[Profiles](https://github.com/murerkinn/bookshelf/blob/main/docs/profiles.md)
who is reading, and where they got to

[Reading in the browser](https://github.com/murerkinn/bookshelf/blob/main/docs/reader.md)
the readers and their controls

[The OPDS catalog](https://github.com/murerkinn/bookshelf/blob/main/docs/opds.md)
reading on a Kobo, a Kindle, or any OPDS client

[Architecture](https://github.com/murerkinn/bookshelf/blob/main/docs/architecture.md)
for working on the code

[What's missing](https://github.com/murerkinn/bookshelf/blob/main/docs/roadmap.md)
limitations, and what's planned

## Contributing

See [CONTRIBUTING.md](https://github.com/murerkinn/bookshelf/blob/main/CONTRIBUTING.md). In short: Node 24,  `npm install` , and
 `npm run lint` ,  `npm run check-types`  and  `npm test`  before you push. Say what
you verified — the tests reach the packages and the app's service layer but not
its pages.

Storage providers are the extension point, and yours doesn't have to live here.
A package published by anyone can be installed and named in the config.

## License

MIT — see [LICENSE](https://github.com/murerkinn/bookshelf/blob/main/LICENSE).

That covers the code in this repository. The app and the Docker image also ship
other people's, under their own terms, listed in
[THIRD-PARTY-NOTICES.md](https://github.com/murerkinn/bookshelf/blob/main/THIRD-PARTY-NOTICES.md).

None of it says anything about the books you put in a library built with it,
whose copyright is between you and their publishers.

## About

Self-hosted ebook library that runs on object storage - a Cloudflare Worker over R2, or a Node server over a directory. No database.

### Topics

[cloudflare-workers](https://github.com/topics/cloudflare-workers)[ebook](https://github.com/topics/ebook)[epub](https://github.com/topics/epub)[self-hosted](https://github.com/topics/self-hosted)

### Resources

[Readme](https://github.com/murerkinn/bookshelf#readme-ov-file)[MIT license](https://github.com/murerkinn/bookshelf#MIT-1-ov-file)

### Contributing

[Contributing](https://github.com/murerkinn/bookshelf#contributing-ov-file)

### Security policy

[Security policy](https://github.com/murerkinn/bookshelf#security-ov-file)[Activity](https://github.com/murerkinn/bookshelf/activity)

### Stars

340 stars

### Watchers

1 watching

### Forks

[12 forks](https://github.com/murerkinn/bookshelf/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fmurerkinn%2Fbookshelf&report=murerkinn+%28user%29)

## Releases

## Used by

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
