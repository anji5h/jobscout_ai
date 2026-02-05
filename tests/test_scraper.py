from bs4 import BeautifulSoup

html = """
<div class="scaffold-layout__list-detail-inner scaffold-layout__list-detail-inner--grow">
    <div class="scaffold-layout__list " tabindex="-1">



        <header class="scaffold-layout__list-header jobs-search-results-list__header--blue
          
          jobs-search-results-list__header ph1
          " tabindex="-1">

            <div class="jobs-search-results-list__title-heading
            truncate
            jobs-search-results-list__text">
                <span id="results-list__title" class="t-16" title="junior software engineer in Estonia" dir="ltr">
                    <!---->junior software engineer in Estonia<!---->
                </span>

                <div class="display-flex flex-column t-12 t-black--light t-normal">
                    <small class="display-flex t-normal
                  t-12 t-black--light
                  
                  jobs-search-results-list__text">
                        <div class="jobs-search-results-list__subtitle
                    ">
                            <span dir="ltr">
                                <!---->613 results<!---->
                            </span>
                            <!----><!---->
                        </div>
                    </small>
                    <!----><!---->
                </div>
            </div>
            <!---->





            <div class="jobs-search-create-alert__wrapper">
                <div>
                    <div id="ember28" class="jobs-search-create-alert__artdeco-toggle jobs-search-create-alert__artdeco-toggle-text artdeco-toggle artdeco-toggle--24dp artdeco-toggle--default ember-view"><span aria-hidden="true" class="artdeco-toggle__text" data-artdeco-toggle-text="true">
                            Set alert
                        </span>
                        <label for="adToggle_ember28" data-artdeco-toggle-label="true" class="artdeco-toggle__label default">
                            <span class="label  a11y-text " data-artdeco-toggle-label-hidden="true">
                                Set job alert for Junior software engineer in Estonia
                            </span>
                        </label>

                        <input role="switch" aria-checked="false" class="input artdeco-toggle__button artdeco-toggle__button--24dp" data-artdeco-toggle-button="true" id="adToggle_ember28" type="checkbox">
                    </div>
                </div>
            </div>

            <!---->

            <span></span>



            <!---->
            <!---->


        </header>

        <div class="JjgciirmrqOWScOJFoPGjAxtbLAEjqpXc
          
          ">

            <!---->


            <button id="ember29" class="artdeco-button artdeco-button--1 artdeco-button--fluid artdeco-button--tertiary ember-view scaffold-layout__list-jump-button" type="button"><!---->
                <span class="artdeco-button__text">
                    Jump to active job details
                </span></button>

            <button id="ember30" class="artdeco-button artdeco-button--1 artdeco-button--fluid artdeco-button--tertiary ember-view scaffold-layout__list-jump-button" type="button"><!---->
                <span class="artdeco-button__text">
                    Jump to active search result
                </span></button>

            <!---->

            <!---->

            <!---->
            <div data-results-list-top-scroll-sentinel=""></div>
            <ul class="hafLCdjlaTvyLKWaIITbTTDRaExRbKY">


                <li id="ember163" class="ember-view   qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4357993609">


                    <div>

                        <div data-job-id="4357993609" class="display-flex job-card-container relative job-card-list
        job-card-container--clickable
        
        job-card-list--underline-title-on-hover jobs-search-results-list__list-item--active jobs-search-two-pane__job-card-container--viewport-tracking-0" aria-current="page">

                            <div>
                                <div id="ember164" class="job-card-list__entity-lockup  artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view">
                                    <div id="ember165" class="job-card-list__logo  artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view" type="square">

                                        <div class="ivm-image-view-model    job-card-list__logo-ivm">

                                            <div class="ivm-view-attr__img-wrapper
        
        ">
                                                <!---->
                                                <!----> <img width="56" src="https://media.licdn.com/dms/image/v2/C4D0BAQEoI6gRul5ZGA/company-logo_100_100/company-logo_100_100/0/1632992687132/turnit_ltd_logo?e=1772064000&amp;v=beta&amp;t=_S2tVlZ4UGc-HYEtIN1cso45lpar2CUdlbWq6WOdqao" loading="lazy" height="56" alt="Turnit logo" id="ember166" class="ivm-view-attr__img--centered EntityPhoto-square-4   evi-image lazy-image ember-view">
                                            </div>

                                        </div>


                                    </div>

                                    <div id="ember167" class="flex-grow-1 artdeco-entity-lockup__content ember-view">
                                        <div id="ember168" class="full-width artdeco-entity-lockup__title ember-view">
                                            <a data-control-id="V76ODcRdouBLHhoi7YjZXQ==" tabindex="0" href="/jobs/view/4357993609/?eBP=CwEAAAGcKNL5yoAHtIDaRTsdj-W4qLiazafZ-PXdomWjVe2Ziq3FVwjY2zQIxgbVBHNN_qlnEVcqk0kdQOKRO5-42oAqsWSg2yuT-brxGXSQr5tqzl6bp1CkcuRKyPvax5YIV7qZzAvBZ_JfnLezgC3K2whRrPJ9OXJe3gA3wIJA1Y8P8xJTsSBVOz5nce8MkhmwmdftdJYoS65-KI9O1xhOp48dA3MBpLRLqDBcuEw4egkA9IpFHrVYZirpcSdUSlRHjfyW7ggn7dwDuHecxL4JMx30bZCkFSHPeab-ZwR4_8deKruk_gm2nJlUMyJWgl6xhY89h-lhbjDf46dNYVgwZFxJo7L1-ShKLCYNc7hPAs7laF4YG9407cRiTxtgMY6QeQB55OxW6nlGFRwAyy9igcE_jle4rw8g_1yFkvn7qPp5ylLzwq-OGICBo3ZoAVW3wSeLNXc7NzmvLYlnCCzIZ-mKWIvFXHS3-UhOTBW9KsGclrCKhlx45lYcvZbKKF9bYIyyaeJtl46iNECZA9Jxy60bGR066cCX5MmT9qhJhSqugdPxnSSyQcGcd0H0wQ&amp;refId=vckJ%2FtJEhvj%2Bm8MFjo%2BIMA%3D%3D&amp;trackingId=V76ODcRdouBLHhoi7YjZXQ%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember169" class="disabled ember-view job-card-container__link
                      YclwhiOAkzknPXgInCXIxAymdsiNRkMapMTqdg
                      job-card-list__title--link" aria-label="Back End Developer" dir="ltr">
                                                <span aria-hidden="true"><strong><!---->Back End Developer<!----></strong></span><span class="visually-hidden"><!---->Back End Developer<!----></span>
                                            </a>

                                        </div>
                                        <div id="ember170" class="artdeco-entity-lockup__subtitle ember-view">
                                            <span class="fGZmAkDyHxLpORwHDqbrwxTdaHBgkfk " dir="ltr">
                                                <!---->Turnit<!---->
                                            </span>

                                        </div>

                                        <div id="ember171" class="artdeco-entity-lockup__caption ember-view">
                                            <ul class="job-card-container__metadata-wrapper">
                                                <li class="kbCgcJFtjhyadWXxnUgjxJYjGMRpikkg ">
                                                    <span dir="ltr">
                                                        <!---->Tartu, Tartumaa, Estonia (On-site)<!---->
                                                    </span>
                                                </li>
                                                <!---->
                                            </ul>
                                        </div>

                                        <!---->
                                        <!---->
                                    </div>


                                </div>



                                <div class="job-card-list__insight">

                                    <div class="display-flex align-items-center t-black--light t-12">
                                        <div class="mv1">

                                            <div class="ivm-image-view-model   ">

                                                <div class="ivm-view-attr__img-wrapper
        
        ">
                                                    <!---->
                                                    <!----> <img width="32" src="https://media.licdn.com/dms/image/v2/C560BAQEZdp64mCX2hw/company-logo_100_100/company-logo_100_100/0/1646207051237/university_of_tartu_logo?e=1772064000&amp;v=beta&amp;t=OEa-EFZ6hjBk5BRw0W3PFjxOYtDJQvkbxGmnSd3Ytlk" loading="lazy" height="32" alt="" id="ember172" class="ivm-view-attr__img--centered EntityPhoto-square-1  job-card-container__job-insight-image evi-image lazy-image ember-view">
                                                </div>

                                            </div>

                                        </div>
                                        <div class="job-card-container__job-insight-text" dir="ltr">
                                            <span aria-hidden="true"><!---->4 company alumni work here<!----></span><span class="visually-hidden"><!---->4 University of Tartu company alumni work here<!----></span>
                                        </div>
                                    </div>

                                </div>


                                <ul class="job-card-list__footer-wrapper job-card-container__footer-wrapper flex-shrink-zero display-flex t-sans t-12 t-black--light t-normal t-roman mt1">
                                    <li class="job-card-container__footer-item job-card-container__footer-job-state t-bold">
                                        Viewed
                                    </li>
                                    <li class="job-card-container__footer-item inline-flex align-items-center">
                                        <span dir="ltr">
                                            <!---->Promoted<!---->
                                        </span>
                                    </li>
                                    <!---->
                                    <li class="FBbRcEuVKISrEbQgsJgfVxwHPvgpOvBwGFIg
                          job-card-container__footer-item inline-flex align-items-center">
                                        <svg role="none" aria-hidden="true" class="job-card-list__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="linkedin-bug-color-small">
                                            <!----> <svg display="var(--hue-web-svg-display-light)">
                                                <image href="https://static.licdn.com/aero-v1/sc/h/cukxdu7s8ldmqz13xdao5xe75" x="0" y="0" width="16" height="16"></image>
                                            </svg>
                                            <svg display="var(--hue-web-svg-display-dark)">
                                                <image href="https://static.licdn.com/aero-v1/sc/h/7qvn5nkkh1mlaqd5xm0radtjv" x="0" y="0" width="16" height="16"></image>
                                            </svg>
                                        </svg>

                                        <span dir="ltr">
                                            <!---->Easy Apply<!---->
                                        </span>
                                    </li>
                                </ul>
                                <span class="visually-hidden" aria-live="polite">
                                    <!----> </span>
                            </div>
                            <div class="job-card-list__actions-container">


                                <div id="ember173" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view job-card-container__actions">
                                    <button aria-expanded="false" aria-label="More options" id="ember174" class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view artdeco-button artdeco-button--1 artdeco-button--tertiary artdeco-button--muted artdeco-button--circle" type="button" tabindex="0">
                                        <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="overflow-web-ios-small">
                                            <!---->
                                            <use href="#overflow-web-ios-small" width="16" height="16"></use>
                                        </svg>


                                        <!----></button>
                                    <div tabindex="-1" aria-hidden="true" id="ember175" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view job-card-container__dropdown-content job-card-actions__overflow-dropdown"><!----></div>
                                </div>


                                <div>
                                    <button aria-label="Dismiss Back End Developer job" id="ember176" class="job-card-container__action job-card-container__action-small artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view" type="button"><!---->
                                        <span class="artdeco-button__text">

                                            <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="close-small">
                                                <!---->
                                                <use href="#close-small" width="16" height="16"></use>
                                            </svg>

                                            <span class="job-card-container__action-text"></span>

                                        </span></button>
                                </div>

                                <!---->
                            </div>
                        </div>

                    </div>


                </li>


                <li id="ember177" class="ember-view   qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4368032147">


                    <div>

                        <div data-job-id="4368032147" class="display-flex job-card-container relative job-card-list
        job-card-container--clickable
        
        job-card-list--underline-title-on-hover  jobs-search-two-pane__job-card-container--viewport-tracking-1">

                            <div>
                                <div id="ember178" class="job-card-list__entity-lockup  artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view">
                                    <div id="ember179" class="job-card-list__logo  artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view" type="square">

                                        <div class="ivm-image-view-model    job-card-list__logo-ivm">

                                            <div class="ivm-view-attr__img-wrapper
        
        ">
                                                <!---->
                                                <!----> <img width="56" src="https://media.licdn.com/dms/image/v2/C4E0BAQEFVyMJ55CkkQ/company-logo_100_100/company-logo_100_100/0/1630616911822/scoro_software_logo?e=1772064000&amp;v=beta&amp;t=6L_J5GZ7EPw26tAY2jfMEpF_e9Xqq5hNgUR9Hkl9Ks0" loading="lazy" height="56" alt="Scoro logo" id="ember180" class="ivm-view-attr__img--centered EntityPhoto-square-4   evi-image lazy-image ember-view">
                                            </div>

                                        </div>


                                    </div>

                                    <div id="ember181" class="flex-grow-1 artdeco-entity-lockup__content ember-view">
                                        <div id="ember182" class="full-width artdeco-entity-lockup__title ember-view">
                                            <a data-control-id="RCMdVD125ADSf2PMT4cW3Q==" tabindex="0" href="/jobs/view/4368032147/?eBP=CwEAAAGcKNL5yjQd799ufXtRpfhC23--8ROr22SSXTfrRpqd_8yO9sTQW5X3iyVZtntYUUZnysRqc4oGtIXp39sAnKHmSvFZb6tDPfonHmLq6SnXifpcnxgbPphSxH2_C9iQkn3UwHZytDVM9fWDCewsAp4rx4QLc00WR3atwdfU_X-0tEfKpzxYAFz-H_w2wA5i3qOfzVNSZnrIy4YtR0MCMPg4LgjlAUxwGtismcDv9B4vfJir3cfPlI1wzLREYgcJhixVGPXCBKsrfVIZPzOKgqvPkjuHSWPyPBRCrkIDoiy_guaL2RSoKeHFlyKvm-7w_yZy_gx0DVN96qhQTx-OIJ3ovvhPh1_azilwc3yT8QZrAhYmb1NgZKX5Uyl8KT3eROrGDfW3BF6cdGL0JHoyjSv7XC-LZVs9HEQojagDs1Lw9owH580K81JCr4WACvaSLUQQJBwF2DxCFlotEymniELNBQm9TU1IOXEZqR-WksQLcOL_alMxLn3xNfxchKfh3WDAORfL4ulAOl-bpHxXlQL2s88qOjlRhbvFF-bho8N0zJWXalP5nlHKTJr6FA&amp;refId=vckJ%2FtJEhvj%2Bm8MFjo%2BIMA%3D%3D&amp;trackingId=RCMdVD125ADSf2PMT4cW3Q%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember183" class="disabled ember-view job-card-container__link
                      YclwhiOAkzknPXgInCXIxAymdsiNRkMapMTqdg
                      job-card-list__title--link" aria-label="Junior Software Engineer" dir="ltr">
                                                <span aria-hidden="true"><strong><!---->Junior Software Engineer<!----></strong></span><span class="visually-hidden"><!---->Junior Software Engineer<!----></span>
                                            </a>

                                        </div>
                                        <div id="ember184" class="artdeco-entity-lockup__subtitle ember-view">
                                            <span class="fGZmAkDyHxLpORwHDqbrwxTdaHBgkfk " dir="ltr">
                                                <!---->Scoro<!---->
                                            </span>

                                        </div>

                                        <div id="ember185" class="artdeco-entity-lockup__caption ember-view">
                                            <ul class="job-card-container__metadata-wrapper">
                                                <li class="kbCgcJFtjhyadWXxnUgjxJYjGMRpikkg ">
                                                    <span dir="ltr">
                                                        <!---->Tallinn, Harjumaa, Estonia (Hybrid)<!---->
                                                    </span>
                                                </li>
                                                <!---->
                                            </ul>
                                        </div>

                                        <!---->
                                        <!---->
                                    </div>


                                </div>



                                <div class="job-card-list__insight">

                                    <div class="display-flex align-items-center t-black--light t-12">
                                        <div class="mv1">

                                            <div class="ivm-image-view-model   ">

                                                <div class="ivm-view-attr__img-wrapper
        
        ">
                                                    <!---->
                                                    <!----> <img width="32" src="https://media.licdn.com/dms/image/v2/C560BAQEZdp64mCX2hw/company-logo_100_100/company-logo_100_100/0/1646207051237/university_of_tartu_logo?e=1772064000&amp;v=beta&amp;t=OEa-EFZ6hjBk5BRw0W3PFjxOYtDJQvkbxGmnSd3Ytlk" loading="lazy" height="32" alt="" id="ember186" class="ivm-view-attr__img--centered EntityPhoto-square-1  job-card-container__job-insight-image evi-image lazy-image ember-view">
                                                </div>

                                            </div>

                                        </div>
                                        <div class="job-card-container__job-insight-text" dir="ltr">
                                            <span aria-hidden="true"><!---->1 company alum works here<!----></span><span class="visually-hidden"><!---->1 University of Tartu company alum works here<!----></span>
                                        </div>
                                    </div>

                                </div>


                                <ul class="job-card-list__footer-wrapper job-card-container__footer-wrapper flex-shrink-zero display-flex t-sans t-12 t-black--light t-normal t-roman mt1">
                                    <li class="job-card-container__footer-item job-card-container__footer-job-state t-bold">
                                        Viewed
                                    </li>
                                    <li class="job-card-container__footer-item inline-flex align-items-center">
                                        <span dir="ltr">
                                            <!---->Promoted<!---->
                                        </span>
                                    </li>
                                    <!---->
                                </ul>
                                <span class="visually-hidden" aria-live="polite">
                                    <!----> </span>
                            </div>
                            <div class="job-card-list__actions-container">


                                <div id="ember187" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view job-card-container__actions">
                                    <button aria-expanded="false" aria-label="More options" id="ember188" class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view artdeco-button artdeco-button--1 artdeco-button--tertiary artdeco-button--muted artdeco-button--circle" type="button" tabindex="0">
                                        <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="overflow-web-ios-small">
                                            <!---->
                                            <use href="#overflow-web-ios-small" width="16" height="16"></use>
                                        </svg>


                                        <!----></button>
                                    <div tabindex="-1" aria-hidden="true" id="ember189" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view job-card-container__dropdown-content job-card-actions__overflow-dropdown"><!----></div>
                                </div>


                                <div>
                                    <button aria-label="Dismiss Junior Software Engineer job" id="ember190" class="job-card-container__action job-card-container__action-small artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view" type="button"><!---->
                                        <span class="artdeco-button__text">

                                            <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="close-small">
                                                <!---->
                                                <use href="#close-small" width="16" height="16"></use>
                                            </svg>

                                            <span class="job-card-container__action-text"></span>

                                        </span></button>
                                </div>

                                <!---->
                            </div>
                        </div>

                    </div>


                </li>


                <li id="ember191" class="ember-view   qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4365239253">


                    <div>

                        <div data-job-id="4365239253" class="display-flex job-card-container relative job-card-list
        job-card-container--clickable
        
        job-card-list--underline-title-on-hover  jobs-search-two-pane__job-card-container--viewport-tracking-2">

                            <div>
                                <div id="ember192" class="job-card-list__entity-lockup  artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view">
                                    <div id="ember193" class="job-card-list__logo  artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view" type="square">

                                        <div class="ivm-image-view-model    job-card-list__logo-ivm">

                                            <div class="ivm-view-attr__img-wrapper
        
        ">
                                                <!---->
                                                <!----> <img width="56" src="https://media.licdn.com/dms/image/v2/D4E0BAQG2vU6lBMHpuA/company-logo_100_100/B4EZjnEDpeGoFI-/0/1756223257643?e=1772064000&amp;v=beta&amp;t=ASgIjWYWyHPTZYrEOi7nkcMOCAVqij1Gux9I1VnfH5s" loading="lazy" height="56" alt="Stellar AI logo" id="ember194" class="ivm-view-attr__img--centered EntityPhoto-square-4   evi-image lazy-image ember-view">
                                            </div>

                                        </div>


                                    </div>

                                    <div id="ember195" class="flex-grow-1 artdeco-entity-lockup__content ember-view">
                                        <div id="ember196" class="full-width artdeco-entity-lockup__title ember-view">
                                            <a data-control-id="m9PEJ8fhN7b3C8R0hWGDYQ==" tabindex="0" href="/jobs/view/4365239253/?eBP=NOT_ELIGIBLE_FOR_CHARGING&amp;refId=vckJ%2FtJEhvj%2Bm8MFjo%2BIMA%3D%3D&amp;trackingId=m9PEJ8fhN7b3C8R0hWGDYQ%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember197" class="disabled ember-view job-card-container__link
                      YclwhiOAkzknPXgInCXIxAymdsiNRkMapMTqdg
                      job-card-list__title--link" aria-label="Junior Software Engineer - Guaranteed Hours Contract Available" dir="ltr">
                                                <span aria-hidden="true"><strong><!---->Junior Software Engineer - Guaranteed Hours Contract Available<!----></strong></span><span class="visually-hidden"><!---->Junior Software Engineer - Guaranteed Hours Contract Available<!----></span>
                                            </a>

                                        </div>
                                        <div id="ember198" class="artdeco-entity-lockup__subtitle ember-view">
                                            <span class="fGZmAkDyHxLpORwHDqbrwxTdaHBgkfk " dir="ltr">
                                                <!---->Stellar AI<!---->
                                            </span>

                                        </div>

                                        <div id="ember199" class="artdeco-entity-lockup__caption ember-view">
                                            <ul class="job-card-container__metadata-wrapper">
                                                <li class="kbCgcJFtjhyadWXxnUgjxJYjGMRpikkg ">
                                                    <span dir="ltr">
                                                        <!---->EMEA (Remote)<!---->
                                                    </span>
                                                </li>
                                                <!---->
                                            </ul>
                                        </div>

                                        <!---->
                                        <!---->
                                    </div>


                                </div>


                                <!---->
                                <ul class="job-card-list__footer-wrapper job-card-container__footer-wrapper flex-shrink-zero display-flex t-sans t-12 t-black--light t-normal t-roman mt1">
                                    <!---->
                                    <li class="job-card-container__footer-item
                              job-card-container__footer-item--highlighted t-bold">
                                        <time datetime="2026-02-03">
                                            21 hours ago
                                            <span class="visually-hidden">Within the past 24 hours</span>
                                        </time>
                                    </li>
                                </ul>
                                <span class="visually-hidden" aria-live="polite">
                                    <!----> </span>
                            </div>
                            <div class="job-card-list__actions-container">


                                <div>
                                    <button aria-label="Dismiss Junior Software Engineer - Guaranteed Hours Contract Available job" id="ember200" class="job-card-container__action job-card-container__action-small artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view" type="button"><!---->
                                        <span class="artdeco-button__text">

                                            <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="close-small">
                                                <!---->
                                                <use href="#close-small" width="16" height="16"></use>
                                            </svg>

                                            <span class="job-card-container__action-text"></span>

                                        </span></button>
                                </div>

                                <!---->
                            </div>
                        </div>

                    </div>


                </li>


                <li id="ember201" class="ember-view   qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4321787789">


                    <div>

                        <div data-job-id="4321787789" class="display-flex job-card-container relative job-card-list
        job-card-container--clickable
        
        job-card-list--underline-title-on-hover  jobs-search-two-pane__job-card-container--viewport-tracking-3">

                            <div>
                                <div id="ember202" class="job-card-list__entity-lockup  artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view">
                                    <div id="ember203" class="job-card-list__logo  artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view" type="square">

                                        <div class="ivm-image-view-model    job-card-list__logo-ivm">

                                            <div class="ivm-view-attr__img-wrapper
        
        ">
                                                <!---->
                                                <!----> <img width="56" src="https://media.licdn.com/dms/image/v2/C4E0BAQGi4FxUQN6fqw/company-logo_100_100/company-logo_100_100/0/1677655590999/wiseaccount_logo?e=1772064000&amp;v=beta&amp;t=j2aDjF4FlN55_P4J1ACTCiMDoR6GcXU70Cnpwo1qgFY" loading="lazy" height="56" alt="Wise logo" id="ember204" class="ivm-view-attr__img--centered EntityPhoto-square-4   evi-image lazy-image ember-view">
                                            </div>

                                        </div>


                                    </div>

                                    <div id="ember205" class="flex-grow-1 artdeco-entity-lockup__content ember-view">
                                        <div id="ember206" class="full-width artdeco-entity-lockup__title ember-view">
                                            <a data-control-id="PcDeHPb6FL/cqCdk4qRbcQ==" tabindex="0" href="/jobs/view/4321787789/?eBP=CwEAAAGcKNL5yrFeVyU4-0Qzu4lwqdUp8f0ZOhk0-7uYgaN8lLTJrg0W8jfME5x2r_Je1v7jjexhCKhOlRsBgUNJM3j7subVtUoxkghNbBitHvqNM7Svj84Mb5p295KAPVUwa3K8FzDheFtizfT-eaoojYvgPwZiP9UemUiAwghtyaVF1zC27a0RsjDjHjdVaNwaxigh_-PQJJCGbyoZFEuXaRvnf-z77P0HwNikm3XsTqPnQCYXa3wNXiKRwfuBQBtm9KJXMzP0_afxq91aEXxIIo9zshzxzOg2zPTjcqGFdH6TrS0f3Lzii6WdztwuTeWrpikU0n2vhoM09glFjT_oJ84FcjC5xws6xzyOaJo-kPeh9AQaqE2UHY5NzW9nCp6uVZUCu_Ut9oyPAeCZZxBYH4kaD8b6fyj8K4vifu3cT9mY94JUeAnoiNB7ms2tZAxt5Ft1w9Mn_ueW2YTXS1OUQfi1IAFyPuJb2SlAzavnVwQDBckPmDBFJJAK2g_fCCF5NRLJzj5taKq21P0FT_EerzhvRqtmxD1Dqqn5aQ&amp;refId=vckJ%2FtJEhvj%2Bm8MFjo%2BIMA%3D%3D&amp;trackingId=PcDeHPb6FL%2FcqCdk4qRbcQ%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember207" class="disabled ember-view job-card-container__link
                      YclwhiOAkzknPXgInCXIxAymdsiNRkMapMTqdg
                      job-card-list__title--link" aria-label="Software Engineer - Treasury Money Movements with verification" dir="ltr">
                                                <span aria-hidden="true"><strong><!---->Software Engineer - Treasury Money Movements<!----></strong><span class="white-space-pre"> </span><!----><!----><span class="tvm__text tvm__text--low-emphasis"><svg role="none" aria-hidden="true" class="text-view-model__verified-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="verified-small">
                                                            <!---->
                                                            <use href="#verified-small" width="16" height="16"></use>
                                                        </svg>
                                                    </span></span><span class="visually-hidden"><!---->Software Engineer - Treasury Money Movements with verification<!----></span>
                                            </a>

                                        </div>
                                        <div id="ember208" class="artdeco-entity-lockup__subtitle ember-view">
                                            <span class="fGZmAkDyHxLpORwHDqbrwxTdaHBgkfk " dir="ltr">
                                                <!---->Wise<!---->
                                            </span>

                                        </div>

                                        <div id="ember209" class="artdeco-entity-lockup__caption ember-view">
                                            <ul class="job-card-container__metadata-wrapper">
                                                <li class="kbCgcJFtjhyadWXxnUgjxJYjGMRpikkg ">
                                                    <span dir="ltr">
                                                        <!---->Tallinn, Harjumaa, Estonia<!---->
                                                    </span>
                                                </li>
                                                <!---->
                                            </ul>
                                        </div>

                                        <!---->
                                        <!---->
                                    </div>


                                </div>



                                <div class="job-card-list__insight">

                                    <div class="display-flex align-items-center t-black--light t-12">
                                        <div class="mv1">

                                            <div class="ivm-image-view-model   ">
                                                <ul class="ivm-image-view-model__img-list--stacked list-style-none display-flex justify-center">
                                                    <li class="ivm-image-view-model__img-list-item--stacked">

                                                        <div class="ivm-view-attr__img-wrapper
        
        ">
                                                            <!---->
                                                            <!----> <img width="32" src="https://media.licdn.com/dms/image/v2/D4E35AQHwmLm8nNw_1g/profile-framedphoto-shrink_100_100/B4EZvCzGTKH8Ak-/0/1768499734015?e=1770818400&amp;v=beta&amp;t=jtnyrjOrRLPMMlPJ6RiZ-l1N99ycwVmy5vKRtXAk5P8" loading="lazy" height="32" alt="" id="ember210" class="ivm-view-attr__img--centered ivm-view-attr__img--stacked ivm-view-attr__img--stacked-circle-size-1 EntityPhoto-circle-1-stackedFacepile  job-card-container__job-insight-image evi-image lazy-image ember-view">
                                                        </div>

                                                    </li>
                                                    <li class="ivm-image-view-model__img-list-item--stacked">

                                                        <div class="ivm-view-attr__img-wrapper
        
        ">
                                                            <!---->
                                                            <!----> <img width="32" src="https://media.licdn.com/dms/image/v2/D4E03AQEd9Cu6HfPxpw/profile-displayphoto-scale_100_100/B4EZgeLEXNGYAg-/0/1752852877588?e=1772064000&amp;v=beta&amp;t=viRzyZcnRxqczxD9YcggF5nwr4jPVjzMsKsoLMOmgOY" loading="lazy" height="32" alt="" id="ember211" class="ivm-view-attr__img--centered ivm-view-attr__img--stacked ivm-view-attr__img--stacked-circle-size-1 EntityPhoto-circle-1-stackedFacepile  job-card-container__job-insight-image evi-image lazy-image ember-view">
                                                        </div>

                                                    </li>
                                                </ul>

                                                <!---->
                                            </div>

                                        </div>
                                        <div class="job-card-container__job-insight-text" dir="ltr">
                                            <!---->2 connections work here<!---->
                                        </div>
                                    </div>

                                </div>


                                <ul class="job-card-list__footer-wrapper job-card-container__footer-wrapper flex-shrink-zero display-flex t-sans t-12 t-black--light t-normal t-roman mt1">
                                    <li class="job-card-container__footer-item job-card-container__footer-job-state t-bold">
                                        Viewed
                                    </li>
                                    <li class="job-card-container__footer-item inline-flex align-items-center">
                                        <span dir="ltr">
                                            <!---->Promoted<!---->
                                        </span>
                                    </li>
                                    <!---->
                                </ul>
                                <span class="visually-hidden" aria-live="polite">
                                    <!----> </span>
                            </div>
                            <div class="job-card-list__actions-container">


                                <div id="ember212" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view job-card-container__actions">
                                    <button aria-expanded="false" aria-label="More options" id="ember213" class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view artdeco-button artdeco-button--1 artdeco-button--tertiary artdeco-button--muted artdeco-button--circle" type="button" tabindex="0">
                                        <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="overflow-web-ios-small">
                                            <!---->
                                            <use href="#overflow-web-ios-small" width="16" height="16"></use>
                                        </svg>


                                        <!----></button>
                                    <div tabindex="-1" aria-hidden="true" id="ember214" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view job-card-container__dropdown-content job-card-actions__overflow-dropdown"><!----></div>
                                </div>


                                <div>
                                    <button aria-label="Dismiss Software Engineer - Treasury Money Movements job" id="ember215" class="job-card-container__action job-card-container__action-small artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view" type="button"><!---->
                                        <span class="artdeco-button__text">

                                            <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="close-small">
                                                <!---->
                                                <use href="#close-small" width="16" height="16"></use>
                                            </svg>

                                            <span class="job-card-container__action-text"></span>

                                        </span></button>
                                </div>

                                <!---->
                            </div>
                        </div>

                    </div>


                </li>


                <li id="ember216" class="ember-view   qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4212310405">


                    <div>

                        <div data-job-id="4212310405" class="display-flex job-card-container relative job-card-list
        job-card-container--clickable
        
        job-card-list--underline-title-on-hover  jobs-search-two-pane__job-card-container--viewport-tracking-4">

                            <div>
                                <div id="ember217" class="job-card-list__entity-lockup  artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view">
                                    <div id="ember218" class="job-card-list__logo  artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view" type="square">

                                        <div class="ivm-image-view-model    job-card-list__logo-ivm">

                                            <div class="ivm-view-attr__img-wrapper
        
        ">
                                                <!---->
                                                <!----> <img width="56" src="https://media.licdn.com/dms/image/v2/D4D0BAQFzZe1y4vbFfw/company-logo_100_100/B4DZap.l18HwAU-/0/1746608480365/betsson_group_logo?e=1772064000&amp;v=beta&amp;t=7v5l51PdNcMQGw6v4TMTOARY2FBnKrQj6asOuXjooJg" loading="lazy" height="56" alt="Betsson Group logo" id="ember219" class="ivm-view-attr__img--centered EntityPhoto-square-4   evi-image lazy-image ember-view">
                                            </div>

                                        </div>


                                    </div>

                                    <div id="ember220" class="flex-grow-1 artdeco-entity-lockup__content ember-view">
                                        <div id="ember221" class="full-width artdeco-entity-lockup__title ember-view">
                                            <a data-control-id="E9QrmouQU95FY0MjDbUZeA==" tabindex="0" href="/jobs/view/4212310405/?eBP=CwEAAAGcKNL5y7exT7K_R86bZzOJVVXeKlwxI3whJsyuiAaMqpNUdW6Q7KKxMMma_lSr6VHDD3g1Fy53qjWTpyV5ECrkzSCMPvY0HN-mhvldw6LAavgDLaTQz5DmUxjyLGkFujb80MC5siUtG4nJ_zn4xdh_IBqqvGThCmw31YpKAqWjfbDh2xKzIrWIyoyXsuDIRShvL7KY1Tw86KsqxnIjvMiRnRSoCf1Ol-OioWztHPJewKbYok6Bmb6RzTim4ZI5cRu0kaCem-958dg4NNNqozGQkN-PGxUvCWjezgK82x5dv6z3UoDzLENYX7EBig2-oI072IFYYtLmDObtkgwFxZNEWjbXagBpBAyadixfENzTknlyuF1Z45GNZU2EpyYqyQUe1xj-z8OuOvgDmsyrBkkdvqHPMF3FNBcqGsPaScvinP4ub1uomaKTXsBlikamyMF_pEvSv1PGT5goX7qgIdm_n8Ne-2R4TTsbPt2qYbJt0xQmz9p0ZnRtMEO52ldZzkoMTfUlv98LcZFaQi37novx6NPV0Ob-rFBiYKN5iS4&amp;refId=vckJ%2FtJEhvj%2Bm8MFjo%2BIMA%3D%3D&amp;trackingId=E9QrmouQU95FY0MjDbUZeA%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember222" class="disabled ember-view job-card-container__link
                      YclwhiOAkzknPXgInCXIxAymdsiNRkMapMTqdg
                      job-card-list__title--link" aria-label="Backend Software Engineer - Web3 with verification" dir="ltr">
                                                <span aria-hidden="true"><strong><!---->Backend Software Engineer - Web3<!----></strong><span class="white-space-pre"> </span><!----><!----><span class="tvm__text tvm__text--low-emphasis"><svg role="none" aria-hidden="true" class="text-view-model__verified-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="verified-small">
                                                            <!---->
                                                            <use href="#verified-small" width="16" height="16"></use>
                                                        </svg>
                                                    </span></span><span class="visually-hidden"><!---->Backend Software Engineer - Web3 with verification<!----></span>
                                            </a>

                                        </div>
                                        <div id="ember223" class="artdeco-entity-lockup__subtitle ember-view">
                                            <span class="fGZmAkDyHxLpORwHDqbrwxTdaHBgkfk " dir="ltr">
                                                <!---->Betsson Group<!---->
                                            </span>

                                        </div>

                                        <div id="ember224" class="artdeco-entity-lockup__caption ember-view">
                                            <ul class="job-card-container__metadata-wrapper">
                                                <li class="kbCgcJFtjhyadWXxnUgjxJYjGMRpikkg ">
                                                    <span dir="ltr">
                                                        <!---->Tallinn, Harjumaa, Estonia (On-site)<!---->
                                                    </span>
                                                </li>
                                                <!---->
                                            </ul>
                                        </div>

                                        <!---->
                                        <!---->
                                    </div>


                                </div>



                                <div class="job-card-list__insight">

                                    <div class="display-flex align-items-center t-black--light t-12">
                                        <div class="mv1">

                                            <div class="ivm-image-view-model   ">

                                                <div class="ivm-view-attr__img-wrapper
        
        ">
                                                    <!---->
                                                    <!----> <img width="32" src="https://media.licdn.com/dms/image/v2/C560BAQEZdp64mCX2hw/company-logo_100_100/company-logo_100_100/0/1646207051237/university_of_tartu_logo?e=1772064000&amp;v=beta&amp;t=OEa-EFZ6hjBk5BRw0W3PFjxOYtDJQvkbxGmnSd3Ytlk" loading="lazy" height="32" alt="" id="ember225" class="ivm-view-attr__img--centered EntityPhoto-square-1  job-card-container__job-insight-image evi-image lazy-image ember-view">
                                                </div>

                                            </div>

                                        </div>
                                        <div class="job-card-container__job-insight-text" dir="ltr">
                                            <span aria-hidden="true"><!---->3 company alumni work here<!----></span><span class="visually-hidden"><!---->3 University of Tartu company alumni work here<!----></span>
                                        </div>
                                    </div>

                                </div>


                                <ul class="job-card-list__footer-wrapper job-card-container__footer-wrapper flex-shrink-zero display-flex t-sans t-12 t-black--light t-normal t-roman mt1">
                                    <li class="job-card-container__footer-item job-card-container__footer-job-state t-bold">
                                        Viewed
                                    </li>
                                    <li class="job-card-container__footer-item inline-flex align-items-center">
                                        <span dir="ltr">
                                            <!---->Promoted<!---->
                                        </span>
                                    </li>
                                    <!---->
                                </ul>
                                <span class="visually-hidden" aria-live="polite">
                                    <!----> </span>
                            </div>
                            <div class="job-card-list__actions-container">


                                <div id="ember226" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view job-card-container__actions">
                                    <button aria-expanded="false" aria-label="More options" id="ember227" class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view artdeco-button artdeco-button--1 artdeco-button--tertiary artdeco-button--muted artdeco-button--circle" type="button" tabindex="0">
                                        <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="overflow-web-ios-small">
                                            <!---->
                                            <use href="#overflow-web-ios-small" width="16" height="16"></use>
                                        </svg>


                                        <!----></button>
                                    <div tabindex="-1" aria-hidden="true" id="ember228" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view job-card-container__dropdown-content job-card-actions__overflow-dropdown"><!----></div>
                                </div>


                                <div>
                                    <button aria-label="Dismiss Backend Software Engineer - Web3 job" id="ember229" class="job-card-container__action job-card-container__action-small artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view" type="button"><!---->
                                        <span class="artdeco-button__text">

                                            <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="close-small">
                                                <!---->
                                                <use href="#close-small" width="16" height="16"></use>
                                            </svg>

                                            <span class="job-card-container__action-text"></span>

                                        </span></button>
                                </div>

                                <!---->
                            </div>
                        </div>

                    </div>


                </li>


                <li id="ember230" class="ember-view   qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4368165886">


                    <div>

                        <div data-job-id="4368165886" class="display-flex job-card-container relative job-card-list
        job-card-container--clickable
        
        job-card-list--underline-title-on-hover  jobs-search-two-pane__job-card-container--viewport-tracking-5">

                            <div>
                                <div id="ember231" class="job-card-list__entity-lockup  artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view">
                                    <div id="ember232" class="job-card-list__logo  artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view" type="square">

                                        <div class="ivm-image-view-model    job-card-list__logo-ivm">

                                            <div class="ivm-view-attr__img-wrapper
        
        ">
                                                <!---->
                                                <!----> <img width="56" src="https://media.licdn.com/dms/image/v2/D4D0BAQFprpI9tmkwfA/company-logo_100_100/company-logo_100_100/0/1696490265118/joinrs_italia_logo?e=1772064000&amp;v=beta&amp;t=aexuFKbnHCiU89QoHvGThyeYIs6uvKCjYfK-2qgFwZk" loading="lazy" height="56" alt="Joinrs logo" id="ember233" class="ivm-view-attr__img--centered EntityPhoto-square-4   evi-image lazy-image ember-view">
                                            </div>

                                        </div>


                                    </div>

                                    <div id="ember234" class="flex-grow-1 artdeco-entity-lockup__content ember-view">
                                        <div id="ember235" class="full-width artdeco-entity-lockup__title ember-view">
                                            <a data-control-id="46EyRBzKGTOIeO6tc+KNpQ==" tabindex="0" href="/jobs/view/4368165886/?eBP=CwEAAAGcKNL5y6a4WuIh6y-jw_PHoKuri-xLRyqgVxqCtVWs7KgUNVlW5oBxNd6_VUqi8icsvskwofmWrYTolXbdwHCtZfh_vqXNj_FLvkg_qTBpri1c4bzRZyfSPhE-EYKu-hB5IaBm98s8afeDR9zBIvGBaJv6U8xQUIlFb49u5KRHCR4aG6fASaGG9_gPjYMlFoofp8wVSayQm63xHwBOnQzqpIXy_iSn3RR5L0DJF_CK5UvHycatW6kgDadJ9QvsUDA0S-GlfPXhLldK8my97P6F7ox2sGT5hBe1WBoMrCGUXUeMsjxRgPBp9cZAuR5n3tIhmxl1uCpEYtH1yeC5L9MZmfGaYTo-hzpXDI-KhBLRfVfSepXISFhpIa6dqsaviCUd8QL75bDas1voW_Iu5T-5VXzG5pi9jAsvv8e-kF1M8aKnGHPoEJs_OTCTpceKCwMmqCx75kO_EDtBeg6DnKReVi86SLVdocEIpWwmh7ZAhEOK2aJ7_qn4SQZQelFsC46Fj5Ahi3L4O1GDiL8EZ4sCfC0&amp;refId=vckJ%2FtJEhvj%2Bm8MFjo%2BIMA%3D%3D&amp;trackingId=46EyRBzKGTOIeO6tc%2BKNpQ%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember236" class="disabled ember-view job-card-container__link
                      YclwhiOAkzknPXgInCXIxAymdsiNRkMapMTqdg
                      job-card-list__title--link" aria-label="Junior Web Developer - EU" dir="ltr">
                                                <span aria-hidden="true"><strong><!---->Junior Web Developer - EU<!----></strong></span><span class="visually-hidden"><!---->Junior Web Developer - EU<!----></span>
                                            </a>

                                        </div>
                                        <div id="ember237" class="artdeco-entity-lockup__subtitle ember-view">
                                            <span class="fGZmAkDyHxLpORwHDqbrwxTdaHBgkfk " dir="ltr">
                                                <!---->Joinrs<!---->
                                            </span>

                                        </div>

                                        <div id="ember238" class="artdeco-entity-lockup__caption ember-view">
                                            <ul class="job-card-container__metadata-wrapper">
                                                <li class="kbCgcJFtjhyadWXxnUgjxJYjGMRpikkg ">
                                                    <span dir="ltr">
                                                        <!---->European Union (Remote)<!---->
                                                    </span>
                                                </li>
                                                <!---->
                                            </ul>
                                        </div>

                                        <!---->
                                        <!---->
                                    </div>


                                </div>


                                <!---->
                                <ul class="job-card-list__footer-wrapper job-card-container__footer-wrapper flex-shrink-zero display-flex t-sans t-12 t-black--light t-normal t-roman mt1">
                                    <!---->
                                    <li class="job-card-container__footer-item inline-flex align-items-center">
                                        <span dir="ltr">
                                            <!---->Promoted<!---->
                                        </span>
                                    </li>
                                    <!---->
                                </ul>
                                <span class="visually-hidden" aria-live="polite">
                                    <!----> </span>
                            </div>
                            <div class="job-card-list__actions-container">


                                <div id="ember239" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view job-card-container__actions">
                                    <button aria-expanded="false" aria-label="More options" id="ember240" class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view artdeco-button artdeco-button--1 artdeco-button--tertiary artdeco-button--muted artdeco-button--circle" type="button" tabindex="0">
                                        <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="overflow-web-ios-small">
                                            <!---->
                                            <use href="#overflow-web-ios-small" width="16" height="16"></use>
                                        </svg>


                                        <!----></button>
                                    <div tabindex="-1" aria-hidden="true" id="ember241" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view job-card-container__dropdown-content job-card-actions__overflow-dropdown"><!----></div>
                                </div>


                                <div>
                                    <button aria-label="Dismiss Junior Web Developer - EU job" id="ember242" class="job-card-container__action job-card-container__action-small artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view" type="button"><!---->
                                        <span class="artdeco-button__text">

                                            <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="close-small">
                                                <!---->
                                                <use href="#close-small" width="16" height="16"></use>
                                            </svg>

                                            <span class="job-card-container__action-text"></span>

                                        </span></button>
                                </div>

                                <!---->
                            </div>
                        </div>

                    </div>


                </li>


                <li id="ember243" class="ember-view   qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4365056488">


                    <div>

                        <div data-job-id="4365056488" class="display-flex job-card-container relative job-card-list
        job-card-container--clickable
        
        job-card-list--underline-title-on-hover  jobs-search-two-pane__job-card-container--viewport-tracking-6">

                            <div>
                                <div id="ember244" class="job-card-list__entity-lockup  artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view">
                                    <div id="ember245" class="job-card-list__logo  artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view" type="square">

                                        <div class="ivm-image-view-model    job-card-list__logo-ivm">

                                            <div class="ivm-view-attr__img-wrapper
        
        ">
                                                <!---->
                                                <!----> <img width="56" src="https://media.licdn.com/dms/image/v2/D4E0BAQGa0fZ2sst4sA/company-logo_100_100/B4EZel8rv7HsAQ-/0/1750835838313/cargoo_com_logo?e=1772064000&amp;v=beta&amp;t=PsfG5s5-KDrY2_H5ALfSsbC2dZoBZKdD3ShXFZvHkAs" loading="lazy" height="56" alt="Cargoo logo" id="ember246" class="ivm-view-attr__img--centered EntityPhoto-square-4   evi-image lazy-image ember-view">
                                            </div>

                                        </div>


                                    </div>

                                    <div id="ember247" class="flex-grow-1 artdeco-entity-lockup__content ember-view">
                                        <div id="ember248" class="full-width artdeco-entity-lockup__title ember-view">
                                            <a data-control-id="Bdgbo06W3KGGpkZUUVyQNg==" tabindex="0" href="/jobs/view/4365056488/?eBP=CwEAAAGcKNL5y4RO7vfcl0H1AsxavNEb_nZdhxOelgYlLoVKd5WNts66H8keevWDUa4bH014C3YMG_XJUfD5q6zPh3DrT3Py968Y-PsAjAG5ViWWSYJEFAcfzDBLi_Ydmt26hHc9ko_5QHKGUGvpLRUqnAZxDPybx-h-wcpRYJIXOmBZBUVSGI7mdY3gL5e2g1LDD8B68zodEvNx3mI50qRR5dqUd-m_mSKldx2huC2FVzGn1zMoeqZzrUhCnxFRM2K2NH7uBBQ5zp3xgU27_mr5CJ2wvIpF_NsXDw3abxExiClV84IhAp9Tb5BG2NCEhZ2BV5Fg_kYSLG31UyB-5sjvpLro_AvPlIDle7pV6dTeh_wENedWm_rPxcenG_SvFFH491Wwt3w1UYLgwD2ZvXqlDO2qkpuC0ygBbVLQtn4fqjIDl0X4cEM_Yvysvh7BWqJTZaslpdIuT87P-8OA0hAXxn4TDW620-rO5oL05qAJ-WRM_9T6C1ey0EUBtHv5fvCyMbIXLE0W_dcD-g_FShP7Z7RFCZCvbQVaXlq7cj5Z&amp;refId=vckJ%2FtJEhvj%2Bm8MFjo%2BIMA%3D%3D&amp;trackingId=Bdgbo06W3KGGpkZUUVyQNg%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember249" class="disabled ember-view job-card-container__link
                      YclwhiOAkzknPXgInCXIxAymdsiNRkMapMTqdg
                      job-card-list__title--link" aria-label="Data Engineer" dir="ltr">
                                                <span aria-hidden="true"><strong><!---->Data Engineer<!----></strong></span><span class="visually-hidden"><!---->Data Engineer<!----></span>
                                            </a>

                                        </div>
                                        <div id="ember250" class="artdeco-entity-lockup__subtitle ember-view">
                                            <span class="fGZmAkDyHxLpORwHDqbrwxTdaHBgkfk " dir="ltr">
                                                <!---->Cargoo<!---->
                                            </span>

                                        </div>

                                        <div id="ember251" class="artdeco-entity-lockup__caption ember-view">
                                            <ul class="job-card-container__metadata-wrapper">
                                                <li class="kbCgcJFtjhyadWXxnUgjxJYjGMRpikkg ">
                                                    <span dir="ltr">
                                                        <!---->Tallinn Metropolitan Area (On-site)<!---->
                                                    </span>
                                                </li>
                                                <!---->
                                            </ul>
                                        </div>

                                        <!---->
                                        <!---->
                                    </div>


                                </div>



                                <div class="job-card-list__insight">

                                    <div class="display-flex align-items-center t-black--light t-12">
                                        <div class="mv1">

                                            <div class="ivm-image-view-model   ">

                                                <div class="ivm-view-attr__img-wrapper
        
        ">
                                                    <!---->
                                                    <!----> <img width="32" src="https://media.licdn.com/dms/image/v2/C560BAQEZdp64mCX2hw/company-logo_100_100/company-logo_100_100/0/1646207051237/university_of_tartu_logo?e=1772064000&amp;v=beta&amp;t=OEa-EFZ6hjBk5BRw0W3PFjxOYtDJQvkbxGmnSd3Ytlk" loading="lazy" height="32" alt="" id="ember252" class="ivm-view-attr__img--centered EntityPhoto-square-1  job-card-container__job-insight-image evi-image lazy-image ember-view">
                                                </div>

                                            </div>

                                        </div>
                                        <div class="job-card-container__job-insight-text" dir="ltr">
                                            <span aria-hidden="true"><!---->3 school alumni work here<!----></span><span class="visually-hidden"><!---->3 University of Tartu school alumni work here<!----></span>
                                        </div>
                                    </div>

                                </div>


                                <ul class="job-card-list__footer-wrapper job-card-container__footer-wrapper flex-shrink-zero display-flex t-sans t-12 t-black--light t-normal t-roman mt1">
                                    <!---->
                                    <li class="job-card-container__footer-item inline-flex align-items-center">
                                        <span dir="ltr">
                                            <!---->Promoted<!---->
                                        </span>
                                    </li>
                                    <!---->
                                </ul>
                                <span class="visually-hidden" aria-live="polite">
                                    <!----> </span>
                            </div>
                            <div class="job-card-list__actions-container">


                                <div id="ember253" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view job-card-container__actions">
                                    <button aria-expanded="false" aria-label="More options" id="ember254" class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view artdeco-button artdeco-button--1 artdeco-button--tertiary artdeco-button--muted artdeco-button--circle" type="button" tabindex="0">
                                        <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="overflow-web-ios-small">
                                            <!---->
                                            <use href="#overflow-web-ios-small" width="16" height="16"></use>
                                        </svg>


                                        <!----></button>
                                    <div tabindex="-1" aria-hidden="true" id="ember255" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view job-card-container__dropdown-content job-card-actions__overflow-dropdown"><!----></div>
                                </div>


                                <div>
                                    <button aria-label="Dismiss Data Engineer job" id="ember256" class="job-card-container__action job-card-container__action-small artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view" type="button"><!---->
                                        <span class="artdeco-button__text">

                                            <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="close-small">
                                                <!---->
                                                <use href="#close-small" width="16" height="16"></use>
                                            </svg>

                                            <span class="job-card-container__action-text"></span>

                                        </span></button>
                                </div>

                                <!---->
                            </div>
                        </div>

                    </div>


                </li>


                <li id="ember257" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4314159111">
                    <!---->
                </li>


                <li id="ember258" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4357742336">
                    <!---->
                </li>


                <li id="ember259" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4367235638">
                    <!---->
                </li>


                <li id="ember260" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4334708253">
                    <!---->
                </li>


                <li id="ember261" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4356042227">
                    <!---->
                </li>


                <li id="ember262" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4357587264">
                    <!---->
                </li>


                <li id="ember263" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4365360514">
                    <!---->
                </li>


                <li id="ember264" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4367834005">
                    <!---->
                </li>


                <li id="ember265" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4357558106">
                    <!---->
                </li>


                <li id="ember266" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4366748330">
                    <!---->
                </li>


                <li id="ember267" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4369070453">
                    <!---->
                </li>


                <li id="ember268" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4356032919">
                    <!---->
                </li>


                <li id="ember269" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4355283382">
                    <!---->
                </li>


                <li id="ember270" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4356456977">
                    <!---->
                </li>


                <li id="ember271" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4318916620">
                    <!---->
                </li>


                <li id="ember272" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4356645613">
                    <!---->
                </li>


                <li id="ember273" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4362715046">
                    <!---->
                </li>


                <li id="ember274" class="ember-view jobs-search-results__job-card-search--generic-occludable-area  qYPyMsoJJADxtxmvchIXejNJlatDOThfDX occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="4366104417">
                    <!---->
                </li>


            </ul>

            <div data-view-name="jobs-search-list-feedback">
                <div class="jobs-list-feedback jobs-list-feedback--background-transparent pr3">
                    <div class="display-flex justify-space-between align-items-center">
                        <div class="jobs-list-feedback--fixed-width">
                            <h2 class="t-16 t-bold">
                                Are these results helpful?
                            </h2>
                            <p class="t-14 t-black--light t-normal">
                                Your feedback helps us improve search results.
                            </p>
                        </div>
                        <div class="flex-shrink-zero">
                            <button id="ember275" class="artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--3 artdeco-button--tertiary ember-view"> <svg role="none" aria-hidden="true" class="artdeco-button__icon " xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-supported-dps="24x24" data-test-icon="thumbs-down-outline-medium">
                                    <!---->
                                    <use href="#thumbs-down-outline-medium" width="24" height="24"></use>
                                </svg>


                                <span class="artdeco-button__text">
                                    Are you finding what you’re looking for? No
                                </span></button>
                            <button id="ember276" class="artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--3 artdeco-button--tertiary ember-view"> <svg role="none" aria-hidden="true" class="artdeco-button__icon " xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-supported-dps="24x24" data-test-icon="thumbs-up-outline-medium">
                                    <!---->
                                    <use href="#thumbs-up-outline-medium" width="24" height="24"></use>
                                </svg>


                                <span class="artdeco-button__text">
                                    Are you finding what you’re looking for? Yes
                                </span></button>
                        </div>
                    </div>
                </div>
                <div id="ember277" class="ember-view"><!----></div>
            </div>

            <div id="jobs-search-results-footer">

                <!---->
                <!---->



                <div id="ember94" class="ember-view   ">
                    <!---->
                </div>




                <!----><!---->
                <div class="jobs-search-pagination jobs-search-results-list__pagination p4">
                    <div class="jobs-search-pagination__spacer"></div>

                    <ul class="jobs-search-pagination__pages">
                        <!----><!---->
                        <li class="jobs-search-pagination__indicator">
                            <button class="jobs-search-pagination__indicator-button jobs-search-pagination__indicator-button--active" aria-current="page" aria-label="Page 1" type="button">
                                <span>1</span>
                            </button>
                        </li>
                        <li class="jobs-search-pagination__indicator">
                            <button class="jobs-search-pagination__indicator-button " aria-label="Page 2" type="button">
                                <span>2</span>
                            </button>
                        </li>
                        <li class="jobs-search-pagination__indicator">
                            <button class="jobs-search-pagination__indicator-button " aria-label="Page 3" type="button">
                                <span>3</span>
                            </button>
                        </li>
                        <li class="jobs-search-pagination__indicator">
                            <button class="jobs-search-pagination__indicator-button" aria-label="Page 4" type="button">
                                <span>…</span>
                            </button>
                        </li>
                    </ul>
                    <p class="jobs-search-pagination__page-state">
                        Page 1 of 25
                    </p>

                    <button aria-label="View next page" id="ember278" class="artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view jobs-search-pagination__button jobs-search-pagination__button--next" type="button"> <svg role="none" aria-hidden="true" class="artdeco-button__icon " xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="chevron-right-small" data-rtl="true">
                            <!---->
                            <use href="#chevron-right-small" width="16" height="16"></use>
                        </svg>


                        <span class="artdeco-button__text">
                            Next
                        </span></button>
                </div>

                <!---->
                <footer class="global-footer-compact
        " aria-label="LinkedIn Footer Content">

                    <div id="ember95" class="ember-view global-footer-compact__occlusion-hint  ">
                        <!---->
                    </div>

                </footer>

            </div>
        </div>



    </div>

    <div class="scaffold-layout__detail
            overflow-x-hidden jobs-search__job-details
            
            " tabindex="-1">


        <!---->
        <div class="jobs-search__job-details--wrapper">
            <div></div>


            <div aria-label="Back End Developer" class="jobs-search__job-details--container
          " data-job-details-events-trigger="">

                <div class="jobs-semantic-search-job-details-wrapper" tabindex="0">
                    <div></div>

                    <!---->
                    <div class="job-view-layout jobs-details">
                        <div>
                            <div class="jobs-details__main-content jobs-details__main-content--single-pane full-width
            ">


                                <!---->

                                <div>

                                    <div class="t-14" tabindex="-1">
                                        <!---->
                                        <div class="relative
          job-details-jobs-unified-top-card__container--two-pane">
                                            <div>
                                                <div class="display-flex align-items-center">
                                                    <div class="display-flex align-items-center flex-1">
                                                        <a class="fgKZYsFeTfrmDWHFOKFPhxynRuxTykI " aria-label="Turnit logo" href="https://www.linkedin.com/company/turnit-ltd/life" data-test-app-aware-link="">

                                                            <div class="ivm-image-view-model   ">

                                                                <div class="ivm-view-attr__img-wrapper
        
        ">
                                                                    <!---->
                                                                    <!----> <img width="32" src="https://media.licdn.com/dms/image/v2/C4D0BAQEoI6gRul5ZGA/company-logo_100_100/company-logo_100_100/0/1632992687132/turnit_ltd_logo?e=1772064000&amp;v=beta&amp;t=_S2tVlZ4UGc-HYEtIN1cso45lpar2CUdlbWq6WOdqao" loading="lazy" height="32" alt="Turnit logo" id="ember304" class="ivm-view-attr__img--centered EntityPhoto-square-1   evi-image lazy-image ember-view">
                                                                </div>

                                                            </div>

                                                        </a>

                                                        <div class="job-details-jobs-unified-top-card__company-name" dir="ltr">
                                                            <a class="fgKZYsFeTfrmDWHFOKFPhxynRuxTykI " target="_self" tabindex="0" href="https://www.linkedin.com/company/turnit-ltd/life" data-test-app-aware-link=""><!---->Turnit<!----></a>
                                                        </div>
                                                    </div>

                                                    <div class="job-details-jobs-unified-top-card__top-buttons">

                                                        <div class="social-share">
                                                            <div id="ember145" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
                                                                <button aria-expanded="false" aria-label="Share" id="ember146" class="social-share__dropdown-trigger artdeco-button artdeco-button--3 artdeco-button--tertiary artdeco-button--circle artdeco-button--muted artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
                                                                    <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-supported-dps="24x24" data-test-icon="share-linkedin-medium" data-rtl="true">
                                                                        <!---->
                                                                        <use href="#share-linkedin-medium" width="24" height="24"></use>
                                                                    </svg>

                                                                    <span class="artdeco-button__text">Share</span>

                                                                    <!----></button>

                                                                <div tabindex="-1" aria-hidden="true" id="ember147" class="social-share__content text-align-left artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
                                                            </div>

                                                            <div>


                                                                <!---->

                                                            </div>

                                                            <!---->

                                                            <!---->
                                                        </div>


                                                        <div id="ember148" class="artdeco-dropdown jobs-options artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">

                                                            <button aria-expanded="false" id="ember149" class="artdeco-button artdeco-button--3 artdeco-button--tertiary artdeco-button--muted artdeco-button--circle artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
                                                                <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-supported-dps="24x24" data-test-icon="overflow-web-ios-medium">
                                                                    <!---->
                                                                    <use href="#overflow-web-ios-medium" width="24" height="24"></use>
                                                                </svg>

                                                                <span class="artdeco-button__text">
                                                                    Show more options
                                                                </span>

                                                                <!----></button>

                                                            <div tabindex="-1" aria-hidden="true" id="ember150" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
                                                        </div>

                                                    </div>
                                                </div>

                                                <div class="display-flex justify-space-between flex-wrap mt2">
                                                    <div class="t-24 job-details-jobs-unified-top-card__job-title">
                                                        <h1 class="t-24 t-bold inline"><a href="/jobs/view/4357993609/?alternateChannel=search&amp;eBP=CwEAAAGcKNL5yoAHtIDaRTsdj-W4qLiazafZ-PXdomWjVe2Ziq3FVwjY2zQIxgbVBHNN_qlnEVcqk0kdQOKRO5-42oAqsWSg2yuT-brxGXSQr5tqzl6bp1CkcuRKyPvax5YIV7qZzAvBZ_JfnLezgC3K2whRrPJ9OXJe3gA3wIJA1Y8P8xJTsSBVOz5nce8MkhmwmdftdJYoS65-KI9O1xhOp48dA3MBpLRLqDBcuEw4egkA9IpFHrVYZirpcSdUSlRHjfyW7ggn7dwDuHecxL4JMx30bZCkFSHPeab-ZwR4_8deKruk_gm2nJlUMyJWgl6xhY89h-lhbjDf46dNYVgwZFxJo7L1-ShKLCYNc7hPAs7laF4YG9407cRiTxtgMY6QeQB55OxW6nlGFRwAyy9igcE_jle4rw8g_1yFkvn7qPp5ylLzwq-OGICBo3ZoAVW3wSeLNXc7NzmvLYlnCCzIZ-mKWIvFXHS3-UhOTBW9KsGclrCKhlx45lYcvZbKKF9bYIyyaeJtl46iNECZA9Jxy60bGR066cCX5MmT9qhJhSqugdPxnSSyQcGcd0H0wQ&amp;refId=vckJ%2FtJEhvj%2Bm8MFjo%2BIMA%3D%3D&amp;trackingId=V76ODcRdouBLHhoi7YjZXQ%3D%3D&amp;trk=d_flagship3_search_srp_jobs" id="ember151" class="ember-view">Back End Developer</a></h1><!---->
                                                    </div>

                                                    <!---->
                                                </div>

                                                <!---->
                                                <div class="job-details-jobs-unified-top-card__primary-description-container">
                                                    <div class="t-black--light mt2 job-details-jobs-unified-top-card__tertiary-description-container">
                                                        <span dir="ltr"><span class="tvm__text tvm__text--low-emphasis"><!---->Tartu, Tartumaa, Estonia<!----></span><span class="tvm__text tvm__text--low-emphasis"><span class="white-space-pre"> </span>·<span class="white-space-pre"> </span></span><span class="tvm__text tvm__text--positive"><strong><span><!---->1 hour ago<!----></span></strong></span><span class="tvm__text tvm__text--low-emphasis"><span class="white-space-pre"> </span>·<span class="white-space-pre"> </span></span><span class="tvm__text tvm__text--low-emphasis"><!---->1 applicant<!----></span>
                                                            <p><span class="tvm__text tvm__text--low-emphasis"><!---->Promoted by hirer<!----></span><span class="tvm__text tvm__text--low-emphasis"><span class="white-space-pre"> </span>·<span class="white-space-pre"> </span></span><span class="tvm__text tvm__text--low-emphasis"><!---->No response insights available yet<!----></span></p>
                                                        </span>
                                                    </div>
                                                </div>

                                                <!---->

                                                <div class="job-details-fit-level-preferences">
                                                    <button tabindex="0" class="artdeco-button artdeco-button--secondary artdeco-button--muted" type="button">
                                                        <span class="tvm__text tvm__text--low-emphasis"><strong><!---->On-site<!----></strong></span>
                                                    </button>
                                                    <button tabindex="0" class="artdeco-button artdeco-button--secondary artdeco-button--muted" type="button">
                                                        <span class="tvm__text tvm__text--low-emphasis"><strong><!---->Full-time<!----></strong></span>
                                                    </button>
                                                    <button tabindex="0" class="artdeco-button artdeco-button--secondary artdeco-button--muted" type="button">
                                                        <span aria-hidden="true"><span class="tvm__text tvm__text--low-emphasis"><strong><svg role="none" aria-hidden="true" class="v-align-middle" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="skills-small">
                                                                        <!---->
                                                                        <use href="#skills-small" width="16" height="16"></use>
                                                                    </svg>
                                                                    <span class="white-space-pre"> </span>5 of 11 skills match<!----></strong></span></span><span class="visually-hidden"><!---->Matches your job preferences, job type is {}.<!----></span>
                                                    </button>
                                                </div>

                                                <div id="ember305" class="ember-view"><!----></div>



                                                <div class="mt4">
                                                    <div class="display-flex">

                                                        <div class="jobs-s-apply jobs-s-apply--fadein inline-flex mr2">

                                                            <div class="jobs-apply-button--top-card">
                                                                <button aria-label="Easy Apply to Back End Developer at Turnit" id="jobs-apply-button-id" class="jobs-apply-button
         artdeco-button artdeco-button--3 artdeco-button--primary ember-view" data-job-id="4357993609" data-live-test-job-apply-button=""> <svg role="none" aria-hidden="true" class="artdeco-button__icon artdeco-button__icon--in-bug" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" data-supported-dps="14x14" data-test-icon="linkedin-bug-xxsmall">
                                                                        <!---->
                                                                        <use href="#linkedin-bug-xxsmall" width="14" height="14"></use>
                                                                    </svg>


                                                                    <span class="artdeco-button__text">
                                                                        Easy Apply
                                                                    </span></button>
                                                            </div>

                                                        </div>


                                                        <span class="visibility-hidden"></span>


                                                        <button class="jobs-save-button
         artdeco-button artdeco-button--secondary artdeco-button--3" type="button">
                                                            <span aria-hidden="true" class="jobs-save-button__text">
                                                                Save
                                                            </span>
                                                            <span class="a11y-text">
                                                                Save Back End Developer at Turnit
                                                            </span>
                                                        </button>

                                                    </div>

                                                    <!---->
                                                    <!---->
                                                    <!----><!---->
                                                </div>

                                                <!---->
                                                <!---->
                                                <!----><!---->
                                                <!---->
                                            </div>

                                            <!---->
                                            <!---->
                                        </div>
                                        <div class="job-details-jobs-unified-top-card__sticky-header
            job-details-jobs-unified-top-card__sticky-header--disabled">
                                            <div class="job-details-jobs-unified-top-card__title-container">
                                                <a data-control-id="V76ODcRdouBLHhoi7YjZXQ==" href="/jobs/view/4357993609/?alternateChannel=search&amp;refId=vckJ%2FtJEhvj%2Bm8MFjo%2BIMA%3D%3D&amp;trackingId=V76ODcRdouBLHhoi7YjZXQ%3D%3D&amp;trk=d_flagship3_search_srp_jobs" id="ember152" class="ember-view">
                                                    <h2 class="t-16 t-black t-bold truncate">
                                                        Back End Developer
                                                    </h2>
                                                </a>
                                                <div class="t-14 truncate">
                                                    Turnit · Tartu, Tartumaa, Estonia (On-site)
                                                </div>
                                            </div>
                                            <div class="job-details-jobs-unified-top-card__sticky-buttons-container">

                                                <div class="jobs-s-apply jobs-s-apply--fadein inline-flex mr2">

                                                    <div class="jobs-apply-button--top-card">
                                                        <button aria-label="Easy Apply to Back End Developer at Turnit" id="jobs-apply-button-id" class="jobs-apply-button
         artdeco-button artdeco-button--2 artdeco-button--primary ember-view" data-job-id="4357993609" data-live-test-job-apply-button=""> <svg role="none" aria-hidden="true" class="artdeco-button__icon artdeco-button__icon--in-bug" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" data-supported-dps="14x14" data-test-icon="linkedin-bug-xxsmall">
                                                                <!---->
                                                                <use href="#linkedin-bug-xxsmall" width="14" height="14"></use>
                                                            </svg>


                                                            <span class="artdeco-button__text">
                                                                Easy Apply
                                                            </span></button>
                                                    </div>

                                                </div>



                                                <button class="jobs-save-button
         mr2 artdeco-button artdeco-button--2 artdeco-button--secondary" aria-expanded="false" type="button">
                                                    <span aria-hidden="true" class="jobs-save-button__text">
                                                        Save
                                                    </span>
                                                    <span class="a11y-text">
                                                        Save Back End Developer at Turnit
                                                    </span>
                                                </button>



                                                <div id="ember154" class="artdeco-dropdown jobs-options artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view inline-flex">

                                                    <button aria-expanded="false" id="ember155" class="artdeco-button artdeco-button--2 artdeco-button--tertiary artdeco-button--muted artdeco-button--circle artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
                                                        <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-supported-dps="24x24" data-test-icon="overflow-web-ios-medium">
                                                            <!---->
                                                            <use href="#overflow-web-ios-medium" width="24" height="24"></use>
                                                        </svg>

                                                        <span class="artdeco-button__text">
                                                            Show more options
                                                        </span>

                                                        <!----></button>

                                                    <div tabindex="-1" aria-hidden="true" id="ember156" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
                                                </div>

                                            </div>
                                        </div>
                                    </div>

                                    <!---->
                                    <!---->
                                </div>


                                <!---->





                                <div class="upsell-premium-custom-section-card__container">
                                    <!---->
                                    <div class="artdeco-card mt4 pv4 ph5">
                                        <!---->
                                        <div class="upsell-premium-custom-section-card__content">
                                            <div class="display-flex flex-column">
                                                <div class="text-align-left">
                                                    <h3 class="upsell-premium-custom-section-card__title">
                                                        <!---->See recent hiring trends for Turnit<!---->
                                                    </h3>
                                                    <p class="upsell-premium-custom-section-card__subheader">
                                                        <!---->Access exclusive applicant insights, see jobs where you have the highest chance of hearing back, and more.<!---->
                                                    </p>
                                                    <a class="fgKZYsFeTfrmDWHFOKFPhxynRuxTykI " href="http://www.linkedin.com/premium/products/?upsellOrderOrigin=Tracking%3Av1%3Apremium_job_details_summary_card%3AJob+Seeker%3AIn-Product&amp;utype=job&amp;referenceId=VG4fuTOkSqi2pv1UqpMthw%3D%3D&amp;isSS=false&amp;destRedirectURL=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3FcurrentJobId%3D4357993609%26distance%3D25.0%26geoId%3D102974008%26keywords%3Djunior%2520software%2520engineer%26origin%3DJOBS_HOME_KEYWORD_HISTORY" data-test-app-aware-link="">
                                                        <span class="upsell-premium-custom-section-card__primary-cta-link">
                                                            <svg role="none" aria-hidden="true" class="mr1" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="premium-chip-v2-small">
                                                                <!---->
                                                                <use href="#premium-chip-v2-small" width="16" height="16"></use>
                                                            </svg>

                                                            <span class="upsell-premium-custom-section-card__primary-cta-link-text">
                                                                <!---->Try Premium for €0<!---->
                                                            </span>
                                                        </span>
                                                    </a>
                                                    <!---->
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>






                                <div class="hidden job-details-module relative">
                                    <!---->
                                    <!---->
                                    <!---->
                                    <!---->
                                    <!---->
                                </div>


                                <!---->
                                <!---->
                                <!---->

                                <div class="job-details-module">
                                    <h2 class="text-heading-large">
                                        People you can reach out to
                                    </h2>
                                    <!---->
                                    <div class="job-details-connections-card mt4
                job-details-people-who-can-help__section--two-pane artdeco-card ph5 pv4">
                                        <div>
                                            <div class="display-flex flex-row align-items-center justify-space-between">
                                                <span class="job-details-people-who-can-help__connections-card-summary">

                                                    <div class="ivm-image-view-model    job-details-people-who-can-help__connections-card-summary-image">
                                                        <ul class="ivm-image-view-model__img-list--stacked list-style-none display-flex justify-center">
                                                            <li class="ivm-image-view-model__img-list-item--stacked">

                                                                <div class="ivm-view-attr__img-wrapper
        
        ">
                                                                    <!---->
                                                                    <!----> <img width="48" src="https://media.licdn.com/dms/image/v2/C560BAQEZdp64mCX2hw/company-logo_100_100/company-logo_100_100/0/1646207051237/university_of_tartu_logo?e=1772064000&amp;v=beta&amp;t=OEa-EFZ6hjBk5BRw0W3PFjxOYtDJQvkbxGmnSd3Ytlk" loading="lazy" height="48" alt="University of Tartu logo" id="ember328" class="ivm-view-attr__img--centered ivm-view-attr__img--stacked ivm-view-attr__img--stacked-square-size-3 EntityPhoto-square-3-stackedFacepile   evi-image lazy-image ember-view">
                                                                </div>

                                                            </li>
                                                        </ul>

                                                        <span class="visually-hidden">University of Tartu logo</span>
                                                    </div>

                                                    <div class="text-body-small" dir="ltr">
                                                        <!---->Company alumni from University of Tartu and others in your network<!---->
                                                    </div>
                                                </span>
                                                <button id="ember329" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view job-details-people-who-can-help__connections-card-summary-card-action"><!---->
                                                    <span class="artdeco-button__text">
                                                        Show all
                                                    </span></button>
                                            </div>


                                            <div id="ember330" class="ember-view"><!----></div>

                                        </div>
                                    </div>

                                    <!---->
                                </div>


                                <!---->

                                <div class="jobs-box--fadein jobs-box--full-width jobs-box--with-cta-large jobs-description
        
        
        
         jobs-description--reformatted
        
         job-details-module">

                                    <!---->
                                    <article class="jobs-description__container
          ">
                                        <div class="jobs-description__content jobs-description-content
            ">
                                            <div class="jobs-box__html-content
              iZtAHJpmTxvNCnJguqUrEQQcDvsfZhTnHdE
              t-14 t-normal
              jobs-description-content__text--stretch" id="job-details" tabindex="-1">
                                                <h2 class="text-heading-large">
                                                    About the job
                                                </h2>

                                                <!---->
                                                <div class="mt4">
                                                    <p dir="ltr">
                                                        <span>
                                                            <p><span><strong><!---->Turnit is looking for a Back-End Developer<!----></strong></span><span class="white-space-pre"> </span>who is passionate about building products that users love. Your job will be to help us revolutionize the public transport industry by building a world-class ticketing system!<!----></p>
                                                        </span><span>
                                                            <p><span><br></span></p>
                                                        </span><span>
                                                            <p><!---->Turnit is a traveltech company developing passenger transport ticketing software for train and bus industry companies all around the world. Our solution is used by industry leaders around the world- in the USA, UK, Norway, Sweden, Lithuania, etc.<!----></p>
                                                        </span><span>
                                                            <p><span><br></span></p>
                                                        </span><span>
                                                            <p><span><strong><!---->Your main day-to-day activities include<!----></strong></span></p>
                                                        </span><span>
                                                            <ul>
                                                                <li><!---->Producing clean, efficient code based on requirements, specifications and designs using the<span class="white-space-pre"> </span><span><strong><!---->.NET framework and C# programming language<!----></strong></span></li>
                                                                <li><!---->Upgrading, configuring and debugging existing systems<!----></li>
                                                                <li><!---->Determining operational feasibility by evaluating analysis, problem definition, requirements, solution development and proposed solutions<!----></li>
                                                                <li><!---->Documenting your work by creating documentation, flowcharts, layouts, diagrams, charts and code comments<!----></li>
                                                                <li><!---->Writing unit tests for major components of<span class="white-space-pre"> </span><span><strong><!---->Turnit Ride<!----></strong></span><span class="white-space-pre"> </span>to ensure robustness, including edge cases, usability and general reliability<!----></li>
                                                                <li><!---->Continuously discovering, evaluating and implementing new technologies to maximize development efficiency<!----></li>
                                                                <li><!---->Helping maintain code quality, structure and automation<!----></li>
                                                                <li><!---->Taking ownership of backend components and contributing to architectural discussions<!----></li>
                                                            </ul>
                                                        </span><span>
                                                            <p><span><br></span></p>
                                                        </span><span>
                                                            <p><span><strong><!---->We would be excited if you match the following<!----></strong></span></p>
                                                        </span><span>
                                                            <ul>
                                                                <li><!---->Proven experience as a Back-End Developer<!----></li>
                                                                <li><!---->Familiarity with<span class="white-space-pre"> </span><span><strong><!---->ASP.NET<!----></strong></span><!---->,<span class="white-space-pre"> </span><span><strong><!---->PostgreSQL<!----></strong></span><span class="white-space-pre"> </span>and common design and architectural patterns<!----></li>
                                                                <li><!---->Ability to use version control systems such as<span class="white-space-pre"> </span><span><strong><!---->Git<!----></strong></span></li>
                                                                <li><!---->Familiarity with different architecture styles and APIs<!----></li>
                                                                <li><!---->Excellent troubleshooting and communication skills<!----></li>
                                                                <li><!---->Attention to detail, a structured approach and strong analytical skills<!----></li>
                                                                <li><!---->Proficient verbal and written<span class="white-space-pre"> </span><span><strong><!---->English<!----></strong></span></li>
                                                                <li><!---->Analytical mindset and logical thinking with a passion for IT<!----></li>
                                                                <li><!---->You have a<span class="white-space-pre"> </span><span><strong><!---->“Get Things Done!”<!----></strong></span><span class="white-space-pre"> </span>attitude<!----></li>
                                                            </ul>
                                                        </span><span>
                                                            <p><span><br></span></p>
                                                        </span><span>
                                                            <p><span><strong><!---->We offer you<!----></strong></span></p>
                                                        </span><span>
                                                            <p><!---->Turnit can offer you everything you need to level up your career -<span class="white-space-pre"> </span><span><strong><!---->remote work, flexibility, independence, competitive salary, great colleagues<!----></strong></span><span class="white-space-pre"> </span>and opportunities to learn and grow more than you might expect. We have a culture of getting things done, while strongly valuing<span class="white-space-pre"> </span><span><strong><!---->work-life balance<!----></strong></span><!---->.<!----></p>
                                                        </span><span>
                                                            <p><!---->We have an office in the heart of<span class="white-space-pre"> </span><span><strong><!---->Tartu<!----></strong></span><!---->, but you can definitely work<span class="white-space-pre"> </span><span><strong><!---->remotely<!----></strong></span><!---->.<!----></p>
                                                        </span>
                                                    </p>
                                                    <!---->
                                                </div>
                                            </div>
                                            <div class="jobs-description__details">
                                                <!---->
                                            </div>
                                        </div>
                                    </article>
                                    <!---->
                                </div>


                                <!---->
                                <!---->
                                <!---->
                                <div id="SALARY" class="jobs-details__salary-main-rail-card">
                                    <!----><!---->
                                </div>



                                <div class="job-details-how-you-match-card__container mb4
        
         job-details-module" id="how-you-match-card-container">
                                    <!---->
                                    <!---->
                                    <!---->
                                    <!---->
                                </div>


                                <!---->
                                <!---->
                                <section class="artdeco-card job-details-module">
                                    <!---->


                                    <section class="jobs-company jobs-box--fadein mb4" data-view-name="job-details-about-company-module">
                                        <div class="jobs-company__box">
                                            <h2 class="text-heading-large">
                                                About the company
                                            </h2>

                                            <div class="display-flex align-items-center mt5">
                                                <div id="ember331" class="artdeco-entity-lockup artdeco-entity-lockup--size-5 ember-view flex-grow-1">
                                                    <div id="ember332" class="artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view" type="square">
                                                        <a href="/company/turnit-ltd/life/" id="ember333" class="ember-view link-without-hover-state inline-block" data-view-name="job-details-about-company-logo-link">
                                                            <img title="Turnit" src="https://media.licdn.com/dms/image/v2/C4D0BAQEoI6gRul5ZGA/company-logo_100_100/company-logo_100_100/0/1632992687132/turnit_ltd_logo?e=1772064000&amp;v=beta&amp;t=_S2tVlZ4UGc-HYEtIN1cso45lpar2CUdlbWq6WOdqao" alt="Turnit company logo" id="ember334" class="evi-image ember-view">
                                                        </a>

                                                    </div>
                                                    <div id="ember335" class="artdeco-entity-lockup__content ember-view flex-grow-1">
                                                        <div id="ember336" class="artdeco-entity-lockup__title ember-view t-20">
                                                            <a href="/company/turnit-ltd/life/" id="ember337" class="ember-view link-without-visited-state inline-block t-black" data-view-name="job-details-about-company-name-link">
                                                                Turnit
                                                            </a>

                                                        </div>
                                                        <div id="ember338" class="artdeco-entity-lockup__subtitle ember-view t-16">
                                                            3,637 followers
                                                        </div>
                                                    </div>

                                                </div>

                                                <button class="follow   artdeco-button artdeco-button--secondary ml5" aria-label="Follow" aria-pressed="false" type="button">
                                                    <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="add-small">
                                                        <!---->
                                                        <use href="#add-small" width="16" height="16"></use>
                                                    </svg>

                                                    <span aria-hidden="true">Follow</span>
                                                </button>

                                            </div>

                                            <div class="t-14 mt5">
                                                Software Development
                                                <span class="jobs-company__inline-information">
                                                    11-50 employees
                                                </span>
                                                <span class="jobs-company__inline-information">
                                                    59 on LinkedIn
                                                </span>
                                            </div>
                                            <p class="jobs-company__company-description text-body-small-open">

                                            <div class="QAJVlaiWGWvcILNfiWFjUTQZffRxcuUE
        inline-show-more-text--is-collapsed
        inline-show-more-text--is-collapsed-with-line-clamp
        
        
        
        " style="-webkit-line-clamp:3;" dir="ltr" tabindex="-1">

                                                Turnit is a travel tech company with more than 20 years of industry experience. We provide mission-critical software technology and consultation to ground-based passenger transport operators. <br><br>Turnit Ride is a comprehensive SaaS platform targeted for operators who require complex route network management, dynamic pricing, and flexible responsiveness to the market situation, maximizing their revenue while streamlining their business processes. <br><br>The platform, delivered as full service, processes more than 20 million passenger segments annually and its services are used by over 40 operators in Europe, Northern America and Africa, including industry leaders such as Vy Group, LTG Link, Bus Eireann, CTM, Lux Express etc

                                                <span class="inline-show-more-text__link-container-collapsed">
                                                    <span>…</span>
                                                    <button class="inline-show-more-text__button
                inline-show-more-text__button--light
                link" aria-expanded="false" role="button" type="button">
                                                        show more
                                                    </button>
                                                </span>

                                                <!---->
                                            </div>

                                            </p>

                                            <!---->
                                            <!---->
                                            <!---->
                                        </div>

                                        <div class="jobs-company__footer text-align-center">
                                            <a href="/company/turnit-ltd/life/" id="ember339" class="ember-view link-without-hover-state block pv3" aria-label="Show more about the company" data-view-name="job-details-about-company-life-link">
                                                Show more
                                            </a>
                                        </div>
                                    </section>


                                </section>

                                <!----><!---->
                            </div>
                        </div>

                        <!---->
                        <!---->

                        <div id="ember158" class="ember-view"><!----></div>

                        <div id="ember159" class="ember-view">
                            <div id="ember160" class="ember-view"><!----></div>
                        </div>



                        <div id="ember161" class="ember-view"><!----></div>


                        <!---->
                        <!---->
                        <!---->

                        <div>

                            <div id="ember162" class="ember-view"><!----></div>

                        </div>
                        <!---->
                        <!----><!---->
                    </div>
                </div>
            </div>
            <!---->
        </div>
    </div>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

jobs = []

job_list = soup.select("li.scaffold-layout__list-item[data-occludable-job-id]")

print(f"Found {len(job_list)} job listings.")

job_id = int(job_list[0].get("data-occludable-job-id"))
print(f"Job ID: {job_id}")
job_link = job_list[0].select_one("a.job-card-list__title--link").get("href")
print(f"Job Link: {job_link}")
job_title = soup.select_one(
    "div.job-details-jobs-unified-top-card__job-title a"
).get_text(strip=True)
print(f"Job Title: {job_title}")
company = soup.select_one("div.job-details-jobs-unified-top-card__company-name a")
company_name = company.get_text(strip=True)
print(f"Company: {company_name}")
company_website = company.get("href")
print(f"Company Website: {company_website}")

job_tertiary_desc = soup.select(
    ".job-details-jobs-unified-top-card__tertiary-description-container span.tvm__text"
)

if len(job_tertiary_desc) > 0:
    job_location = job_tertiary_desc[0].get_text(strip=True)
    print(f"Location: {job_location}")
    job_posted_date = job_tertiary_desc[2].get_text(strip=True)
    print(f"Posted Date: {job_posted_date}")

container = soup.select_one("article.jobs-description__container")

if container:
    job_details = container.get_text(separator="\n", strip=True)
    print(job_details)
