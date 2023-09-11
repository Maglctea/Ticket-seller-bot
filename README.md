# Ticket-seller-bot (aiogram bot)

## Download
```bash
git clone https://github.com/Maglctea/Ticket-seller-bot.git
```

## installation
1. Open project folder
2. Create/edit `.env` file (template in `.env.simle`)
### Docker
```bash
docker build -t ticketbot .
docker run --name ticketbot --restart always ticketbot
```

### Without docker
```bash 
pip install -r requirements.txt
python -m bot
```

## Documentation
`/start` - start working with bot