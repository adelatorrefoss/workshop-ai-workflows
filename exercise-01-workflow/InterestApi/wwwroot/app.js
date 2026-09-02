const form = document.querySelector('#registration');
const message = document.querySelector('#message');
form.addEventListener('submit', async event => {
  event.preventDefault();
  const body = Object.fromEntries(new FormData(form).entries());
  const response = await fetch('/api/register', {
    method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(body)
  });
  message.textContent = response.ok ? 'Registration saved' : 'Registration failed';
});
