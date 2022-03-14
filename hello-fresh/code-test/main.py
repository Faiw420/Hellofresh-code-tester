from discord_webhook import DiscordWebhook, DiscordEmbed


webhook = DiscordWebhook(url='https://discord.com/api/webhooks/951139821714305055/I4qbPKgZ96-VGf5EFdFVqC68I_jnUErWOX4Vt6gZKAB-oqzjDiARfu7zB4MMWd-0gnBN', rate_limit_retry = True)

embed = DiscordEmbed(title = "HelloFresh-Code-Tester", description = "Folgender Code funktioniert: ", color='00ff00')
embed.set_author(name="Faiw#0478", url = "https://images-ext-2.discordapp.net/external/fBzmC1958TJQ6loO5U5cS2wRG9uMCAraE1Z-Kxv3Jbc/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/238622878394875905/0e37e24d8a7a79099bd08a7e7379adf8.png", icon_url = "https://images-ext-2.discordapp.net/external/fBzmC1958TJQ6loO5U5cS2wRG9uMCAraE1Z-Kxv3Jbc/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/238622878394875905/0e37e24d8a7a79099bd08a7e7379adf8.png")
embed.set_image(url= "https://images-ext-2.discordapp.net/external/fBzmC1958TJQ6loO5U5cS2wRG9uMCAraE1Z-Kxv3Jbc/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/238622878394875905/0e37e24d8a7a79099bd08a7e7379adf8.png")
embed.set_footer(text="Hellofresh-Code-Tester")
embed.set_timestamp()
webhook.add_embed(embed)
response = webhook.execute()

def createWebhook():
  webhook = DiscordWebhook(url='https://discord.com/api/webhooks/951139821714305055/I4qbPKgZ96-VGf5EFdFVqC68I_jnUErWOX4Vt6gZKAB-oqzjDiARfu7zB4MMWd-0gnBN', rate_limit_retry = True)

  embed = DiscordEmbed(title = "HelloFresh-Code-Tester", description = "Folgender Code funktioniert: ", color='00ff00')
  embed.set_author(name="Faiw#0478", url = "https://images-ext-2.discordapp.net/external/fBzmC1958TJQ6loO5U5cS2wRG9uMCAraE1Z-Kxv3Jbc/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/238622878394875905/0e37e24d8a7a79099bd08a7e7379adf8.png",     icon_url = "https://images-ext-2.discordapp.net/external/fBzmC1958TJQ6loO5U5cS2wRG9uMCAraE1Z-Kxv3Jbc/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/238622878394875905/0e37e24d8a7a79099bd08a7e7379adf8.png")
  embed.set_image(url= "https://images-ext-2.discordapp.net/external/fBzmC1958TJQ6loO5U5cS2wRG9uMCAraE1Z-Kxv3Jbc/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/238622878394875905/0e37e24d8a7a79099bd08a7e7379adf8.png")
  embed.set_footer(text="Hellofresh-Code-Tester")
  embed.set_timestamp()
  webhook.add_embed(embed)
  response = webhook.execute()


