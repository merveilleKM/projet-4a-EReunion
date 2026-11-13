# Version de typescript utilise
npm install -D typescript@5.9

# projet-4a---EReunion-

Application web de suivi de réunion à partir de vidéos (projet 4A, Polytech Dijon).
Elle permet de visionner un enregistrement, de le découper en blocs liés aux interventions des participants, et de retrouver rapidement une information.

## Prérequis

- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (lancé avant toute commande)
- [Node.js](https://nodejs.org/) 20 ou plus (pour le développement du frontend)

## Installation

```powershell
git clone <url-du-depot>
cd <dossier-du-depot>
Copy-Item .env.example .env
docker compose up --build
```

Sous Linux ou macOS, remplacer `Copy-Item .env.example .env` par `cp .env.example .env`.

## Adresses utiles

| Service | Adresse |
|---|---|
| API (état de santé) | http://localhost:8000/health |
| Documentation de l'API (Swagger) | http://localhost:8000/docs |
| Base de données PostgreSQL | `localhost:5432` |

## Commandes utiles

```powershell
docker compose up --build     # démarrer (et reconstruire si besoin)
docker compose down           # arrêter
docker compose down -v        # arrêter ET supprimer la base de données
docker compose logs -f api    # suivre les logs de l'API
```

## Structure du dépôt

```
backend/    API FastAPI (Python)
frontend/   Interface React (TypeScript)
docs/       Documentation, schémas
storage/    Vidéos téléversées (non versionné)
```

## Organisation du travail

- Une branche par fonctionnalité (`feature/...`, `fix/...`, `docs/...`, `infra/...`).
- Aucun commit direct sur `main` : tout passe par une Pull Request relue par l'autre membre.
- Voir le guide Git dans `docs/` pour les conventions de nommage.