const input_area = document.getElementById('input');
const output_area = document.getElementById('output');
input_area.addEventListener('input', update);

function update() {
	let text = input_area.value;
	let form_data = new FormData();
	form_data.append("input", text);
	fetch("/display", {
		"method": "POST", 
		"body": form_data,})
		.then(response => response.json())
		.then(data => {
			output_area.value = data.output;
		})
		.catch(error => {
			console.error(error);
			output_area.value = "An error occured";
		});
}
