const display = async (evt, outputController) => {
	const {status, data} = await Translater.get(evt.target.value);

	if (status) {
		outputController.update(data);
	} else {
		outputController.error();
	}
};