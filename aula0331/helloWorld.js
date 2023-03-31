const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Contet-Type', 'text/plain');
  res.end('Hello World!\n');
});

server.listen(3000, () => {
  console.log('Servidor rodando na porta 3000.');
});