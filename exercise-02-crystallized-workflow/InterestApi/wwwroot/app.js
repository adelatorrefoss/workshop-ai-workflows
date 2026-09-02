const form = document.querySelector('#registration');
form.addEventListener('submit', async event => { event.preventDefault(); const body = Object.fromEntries(new FormData(form).entries()); await fetch('/api/register', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(body)}); });
