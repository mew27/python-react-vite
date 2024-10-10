# React + TypeScript + Vite

Questa repository fa il setup di un progetto di un applicazione desktop che fa uso di python come backend e di React, Vite e Typescript come frontend.

## Setup

Clona questa repository:

`git clone git@github.com:mew27/python-react-vite.git`

Il comando sopra crea la cartella *python-react-vite* che contiene tutta la repository.

Spostati nella cartella repository ed inizializza yarn e l'ambiente python:

```
cd python-react-vite
yarn
```

I comandi sopra installano tutte le dipendenze yarn, creano l'ambiente virtuale python env, attivano l'ambiente virtuale python e ci installano tutte le dipendenze.

## Esegui e compila solo il frontend
Per eseguire il fronted:

`yarn dev`

Per compilare il front-end:

`yarn build`

I file risultanti dalla compilazione sono nella cartella dist.

## Esegui e compila l'intera applicazione
Per eseguire l'intera applicazione (front-end e back-end pyhton):

`yarn python:dev`

Per compilare l'applicazione in unico eseguibile standalone (.exe):

`yarn python:build`

L'eseguibile risultate dalla compilazione si trova nella cartella executables.
