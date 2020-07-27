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

})