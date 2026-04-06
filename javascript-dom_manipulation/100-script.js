document.addEventListener('DOMContentLoaded', () => {

	const add_item = document.getElementById("add_item");
	const remove_item = document.getElementById("remove_item");
	const clear_list = document.getElementById("clear_list");
	const my_list = document.querySelector(".my_list");
	add_item.addEventListener("click", () => {
		const newLi = document.createElement("li");
		newLi.textContent = "Item";
		my_list.appendChild(newLi);

	});
	remove_item.addEventListener("click", () => {
		const lastLi = my_list.lastElementChild;
		if (lastLi) {
			lastLi.remove();
		}

	});
	clear_list.addEventListener("click", () => {
		my_list.innerHTML = '';
	});
});
