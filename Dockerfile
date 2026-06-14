FROM node:18-alpine

WORKDIR /app

ENV NODE_ENV=production
ENV PORT=5000

COPY package*.json ./

RUN npm ci --only=production

COPY . .

EXPOSE 5000

CMD ["npm", "start"]