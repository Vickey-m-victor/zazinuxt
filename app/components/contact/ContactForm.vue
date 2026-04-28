<template>
    <!--==============================
    Contact Area
    ==============================-->
    <section class=" space-extra-bottom ">
        <div class="container">
            <div class="row flex-row-reverse gx-60 justify-content-between">
                <div class="col-xl-auto">
                    <img src="/img/about/con-2-1.png" alt="girl" class="w-100">
                </div>
                <div class="col-xl col-xxl-6 align-self-center">
                    <div class="title-area">
                        <span class="sec-subtitle">Have Any questions? so plese</span>
                        <h2 class="sec-title">Feel Free to Contact!</h2>
                    </div>
                    <form action="https://html.vecurosoft.com/kiddino/demo/mail.php" class="form-style3 layout2 ajax-contact">
                        <div class="row justify-content-between">
                            <div class="col-md-6 form-group">
                                <label>First Name <span class="required">(Required)</span></label>
                                <input name="firstname" id="firstname" type="text">
                            </div>
                            <div class="col-md-6 form-group">
                                <label>Last Name <span class="required">(Required)</span></label>
                                <input name="lastname" id="lastname" type="text">
                            </div>
                            <div class="col-md-6 form-group">
                                <label>Email Address <span class="required">(Required)</span></label>
                                <input name="email" id="email" type="email">
                            </div>
                            <div class="col-md-6 form-group">
                                <label>Phone Number <span class="required">(Required)</span></label>
                                <input name="number" id="number" type="number">
                            </div>
                            <div class="col-12 form-group">
                                <label>Message <span class="required">(Required)</span></label>
                                <textarea name="message" id="message" cols="30" rows="10"
                                    placeholder="Type your message"></textarea>
                            </div>
                            <div class="col-auto form-group">
                                <button class="vs-btn" type="submit">Send Message</button>
                            </div>
                            <p class="form-messages"></p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>
