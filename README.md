# DipDup Tutorial

Materials for the video tutorial [How to build a backend for your Tezos dapp](https://www.youtube.com/watch?v=K-1s6fCBegc)

## Requirements

* Python 3.10+
* Poetry
* Node.js 14+
* Yarn
* Docker
* Docker-compose

## Build & run

#### Indexer

```
docker-compose up -d --build
```

#### SDK

```
yarn
yarn build
yarn link
```

#### UI

```
yarn
yarn link demo-sdk
yarn serve
```
