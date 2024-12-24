const display = async (evt, outputController) => {
	const {status, data} = await Converter.get(evt.target.value);

	if (status) {
		outputController.update(data);
	} else {
		outputController.error();
	}
};
