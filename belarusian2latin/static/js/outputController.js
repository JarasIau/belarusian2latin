class OutputController {
    constructor(outputId) {
        this._errorIsInit = false;
        this._outputEl = document.getElementById(outputId);
    }

    update(newValue) {
        if (this._errorIsInit) {
            this._outputEl.style.color = "black";
            this._errorIsInit = false;
        }

        this._outputEl.innerText = newValue;
    }

    error() {
        this._outputEl.innerText = "An error occured";
        this._outputEl.style.color = "red";
    }
}