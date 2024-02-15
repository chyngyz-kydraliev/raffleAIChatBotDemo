
let ACTIONS = {
    "PurchaseTicketProcess": renderTicketsPurchaseForm,
    "RequiredInformation": renderRegistrationForm,
    "ParticipationSteps": renderRegistrationForm,
    "TicketPurchaseLimit": renderTicketsPurchaseForm
}


function handleActionOnIntent(intent, action_performed_result) {
    let action_handler = ACTIONS[intent];
    if (action_handler) {
        return action_handler(action_performed_result);
    }
}


function renderRegistrationForm() {
    let form = `
    <form>
        <div class="form-row">
            <div class="form-group col-md-12">
                <label for="inputEmail4">Email</label>
                <input type="email" class="form-control" id="inputEmail4" placeholder="Email">
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-12">
                <label for="inputWallet">Crypto Wallet</label>
                <input type="text" class="form-control" id="inputWallet" placeholder="Crypto Wallet">
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-12">
                <label for="inputFullName">Full Name</label>
                <input type="text" class="form-control" id="inputFullName" placeholder="Full Name">
            </div>
        </div>
        <div class="form-row">
            <a href="#" class="btn btn-primary">Submit registration</a>
        </div>
    </form>
    `
    return form;
}


function renderTicketsPurchaseForm(action_performed_result) {

    let tickets = action_performed_result["tickets"]
    let tickets_to_render = ""

    for (let ticket of tickets) {
        let ticket_name = ticket["name"]
        let ticket_price = ticket["price"]
        let ticket_description = ticket["description"]
        let ticket_image = ticket["image"]

        let ticket_card = `
            <div class="col-md-4">
                <div class="card">
                    <img src="${ticket_image}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">${ticket_name}</h5>
                        <p class="card-text">${ticket_description}</p>
                        <p class="card-text">${ticket_price}</p>
                        <a href="#" class="btn btn-primary">Purchase</a>
                    </div>
                </div>
            </div>`
        tickets_to_render += ticket_card
    }

    let rendered_cards = `
        <div class="container">
            <div class="row">
            ${tickets_to_render}
            </div>
        </div>
    `;
    return rendered_cards;
}