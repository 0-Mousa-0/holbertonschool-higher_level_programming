document.addEventListener('DOMContentLoaded', () => {

	const languageCode = document.getElementById("language_code");
	const translateBtn = document.getElementById("btn_translate");
	const hello = document.getElementById("hello");

	translateBtn.addEventListener('click', () => {

		const langcode = languageCode.value;
		if (!langcode) {
			alert('Please select a language!');
			return;
		}
		const apiUrl = `https://hellosalut.stefanbohacek.com/?lang=${langcode}`;
		fetch(apiUrl)
			.then(Response => Response.json())
			.then(data => {
				hello.textContent = data.hello;
			})
			.catch(error => {
				console.log('Error:', error);
				hello.textContent = 'Error loading translation';
			});


	});

});
