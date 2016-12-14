/**
 * Created by shaur on 28-08-2016.
 */

$(document).ready(function(){
    function startupPushNotifications() {
        Pusher.logToConsole = true;

        var pusher = new Pusher('e64252df238c8822e820', {
            encrypted: true
        });

        var channel = pusher.subscribe('inventory');
        channel.bind('user-note', function (data) {
            $('#usr-note').prepend("<li>"+data.message+"</li>")
            console.log(data);
        });
    }


    /* Startup App */
    startupPushNotifications()

});