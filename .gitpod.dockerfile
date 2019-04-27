FROM gitpod/workspace-full
# Install image generator
USER root
RUN apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config python3-dev

ENV IP=0.0.0.0
ENV PORT=3000
ENV DATABASE_URL=postgres://gitpod@127.0.0.1/django-rest-hello
