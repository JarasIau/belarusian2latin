class Translater {

    static async get(text) {
        const formData = new FormData();
        formData.append("input", text);

        const
            res = await fetch("/display", {"method": "POST", "body": formData}),
            status = res.ok,
            data = (await res.json()).output;

        return { status, data };
    }
}