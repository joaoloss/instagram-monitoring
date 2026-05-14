# Requisitos da aplicação

Os requisitos/eventos que a aplicação deve atender.

## Tópico Kafka

O tópico pode se chamar "post-stats" e conter mensagens no seguinte formato:

```json
{
  "id": "123",
  "views": 1200,
  "likes": 180,
  "comments": 42
}
```

## Evento Primitivo

Pode ser um só de acordo com a especificação.

### Post publicado

- Identificador do post
- Número de views
- Número de curtidas
- Número de comentários

## Situações de Interesse

Tem que ser 3 situações de interesse que consomem o evento primitivo.

### Estátisticas dos útimos N posts atualizadas (por tópico)

- N ajustável
- Média
- Desvio padrão
- Exibir distribuição?

### Post viral detectado

- Pode ser o **evento composto** (devolve um evento pro Kafka)
- Deve ser um outlier em relação a todos posts coletados
- Views e/ou curtidas > mi + 1.5 * desvio padrão

### Engajamento caiu

- Média de views dos últimos M posts caindo
- M ajustável e menor que N
- Média de views < mi - 1.5 * desvio padrão
