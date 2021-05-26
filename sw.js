self.addEventListener('push', (e) => {
    const data = e.data.json();
    self.registration.showNotification(data.title,  {body: data.body, requireInteraction: true, icon:'https://localhost:4443/favicon.ico'}   );
});