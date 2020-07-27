const Discord = require('discord.js');
const bot = new Discord.Client();

const token = 'NzM3MzI1NjYzOTA4MDAzOTEx.Xx7uCQ.CVEydvOYz9jZQ8Ayf8p8IwbeSBI';
const PREFIX = '$';

var version = 'BETA';
var devman = 'catter1';
var botname = 'MTG Bot';

bot.on('ready', () =>{
    console.log('You just started up the MTG Bot! Good job.');
})

bot.on('message', message=>{

    if (message.author.bot || !message.content.startsWith(PREFIX)) return;
    const args = message.content.slice(PREFIX.length).split(" ");

    switch(args[0]){
    case 'dev':
        const dev = new Discord.MessageEmbed()
        .setTitle('MTG Bot Information')
        .setAuthor('catter1', 'https://cdn.discordapp.com/avatars/260929689126699008/a_ee5677ca4e913dc06e0408f792ddc44a.webp?size=128')
        .setColor(0x28F5D6)
        .setThumbnail('https://lh3.googleusercontent.com/oaLVuSSzLXtUvyh0L0itUk4LtD7zLPgSOluLJvvklfyqiTMBxwJuToXf0sDCNICuLm67aQ=s85')
        .addField('Bot', botname)
        .addField('Version', version)
        .addField('Developer', devman)
        message.channel.send(dev);
    break;
    }
})

bot.login(token);