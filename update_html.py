import os
import re
import sys

# Change standard output encoding to utf-8 to avoid charmap errors
sys.stdout.reconfigure(encoding='utf-8')

header_replacement = """        <!-- Start header -->
        <header id="header">
            <div class="wpo-site-header wpo-site-header-s1">
                <nav class="navigation navbar navbar-expand-lg navbar-light">
                    <div class="container-fluid">
                        <div class="row align-items-center">
                            <div class="col-lg-3 col-md-4 col-3 d-lg-none dl-block">
                                <div class="mobail-menu">
                                    <button type="button" class="navbar-toggler open-btn" aria-expanded="false" aria-controls="navbar" aria-label="Open menu">
                                        <span class="sr-only">Toggle navigation</span>
                                        <span class="icon-bar first-angle"></span>
                                        <span class="icon-bar middle-angle"></span>
                                        <span class="icon-bar last-angle"></span>
                                    </button>
                                </div>
                            </div>
                            <div class="col-lg-2 col-md-4 col-6">
                                <div class="navbar-header">
                                    <a class="navbar-brand" href="{ROOT_PATH}index.html" aria-label="Anna Clerk Foundation — Home">
                                        <img src="{ROOT_PATH}assets/images/logo.png" style="height:85px;width:auto;object-fit:contain;" alt="Anna Clerk Foundation logo">
                                    </a>
                                </div>
                            </div>
                            <div class="col-lg-7 col-md-1 col-1">
                                <div id="navbar" class="collapse navbar-collapse navigation-holder">
                                    <button class="menu-close" aria-label="Close menu"><i class="ti-close"></i></button>
                                    <ul class="nav navbar-nav mb-2 mb-lg-0">
                                        <li><a href="{ROOT_PATH}index.html">Home</a></li>
                                        <li><a href="{ROOT_PATH}our-work.html">Our Work</a></li>
                                        <li><a href="{ROOT_PATH}event.html">Stories</a></li>
                                        <li class="has-dropdown">
                                            <a href="{ROOT_PATH}our-funding.html" class="nav-dropdown-toggle">Funding</a>
                                            <ul class="ac-dropdown">
                                                <li><a href="{ROOT_PATH}our-funding.html">Funding Approach</a></li>
                                                <li><a href="{ROOT_PATH}supporting-our-work.html">Supporting Our Work</a></li>
                                            </ul>
                                        </li>
                                        <li class="has-dropdown">
                                            <a href="{ROOT_PATH}about.html" class="nav-dropdown-toggle">About Us</a>
                                            <ul class="ac-dropdown">
                                                <li><a href="{ROOT_PATH}about.html">About the Foundation</a></li>
                                                <li><a href="{ROOT_PATH}how-we-work.html">How We Work</a></li>
                                                <li><a href="{ROOT_PATH}faq.html">FAQ</a></li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="col-lg-3 col-md-3 col-2">
                                <div class="header-right">
                                    <div class="close-form">
                                        <a class="theme-btn" href="{ROOT_PATH}our-work.html"><span class="text">Explore our work</span></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </nav>
            </div>
        </header>
        <!-- end of header -->"""

footer_replacement = """        <!-- Stories CTA (replaces fake newsletter) -->
        <section class="ac-stories-cta">
            <div class="container">
                <h3>Explore stories and learning notes</h3>
                <p>Read about the people and organizations leading important work across Vietnam.</p>
                <a href="{ROOT_PATH}event.html">Browse all stories</a>
            </div>
        </section>

        <!-- Footer -->
        <footer class="wpo-site-footer">
            <div class="wpo-upper-footer">
                <div class="container">
                    <div class="row">
                        <div class="col col-lg-4 col-md-6 col-sm-12 col-12">
                            <div class="widget about-widget">
                                <div class="logo" style="margin-bottom: 20px;">
                                    <a href="{ROOT_PATH}index.html" aria-label="Anna Clerk Foundation — Home">
                                        <img src="{ROOT_PATH}assets/images/logo.png" style="height:60px;width:auto;object-fit:contain;" alt="Anna Clerk Foundation logo">
                                    </a>
                                </div>
                                <p>A philanthropic concept exploring practical ideas, trusted local organizations, and communities working toward progress that lasts.</p>
                                <p class="ac-project-note">Anna Clerk Foundation is a fictional philanthropy concept. External stories are shared as credited learning references.</p>
                            </div>
                        </div>
                        <div class="col col-lg-2 col-md-6 col-sm-12 col-12">
                            <div class="widget link-widget">
                                <div class="widget-title"><h3>Explore</h3></div>
                                <ul>
                                    <li><a href="{ROOT_PATH}index.html">Home</a></li>
                                    <li><a href="{ROOT_PATH}our-work.html">Our Work</a></li>
                                    <li><a href="{ROOT_PATH}event.html">Stories</a></li>
                                    <li><a href="{ROOT_PATH}our-funding.html">Funding</a></li>
                                    <li><a href="{ROOT_PATH}about.html">About Us</a></li>
                                </ul>
                            </div>
                        </div>
                        <div class="col col-lg-3 col-md-6 col-sm-12 col-12">
                            <div class="widget link-widget s2">
                                <div class="widget-title"><h3>Focus Areas</h3></div>
                                <ul>
                                    <li><a href="{ROOT_PATH}our-work.html#learning">Learning &amp; Opportunity</a></li>
                                    <li><a href="{ROOT_PATH}our-work.html#climate">Climate &amp; Resilience</a></li>
                                    <li><a href="{ROOT_PATH}our-work.html#health">Health &amp; Well-being</a></li>
                                    <li><a href="{ROOT_PATH}our-work.html#arts">Arts &amp; Civic Life</a></li>
                                </ul>
                            </div>
                        </div>
                        <div class="col col-lg-3 col-md-6 col-sm-12 col-12">
                            <div class="widget link-widget">
                                <div class="widget-title"><h3>More</h3></div>
                                <ul>
                                    <li><a href="{ROOT_PATH}how-we-work.html">How We Work</a></li>
                                    <li><a href="{ROOT_PATH}supporting-our-work.html">Supporting Our Work</a></li>
                                    <li><a href="{ROOT_PATH}faq.html">FAQ</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="wpo-lower-footer">
                <div class="container">
                    <div class="row align-items-center">
                        <div class="col col-lg-12 col-md-12 col-12">
                            <ul style="text-align: center;">
                                <li>&copy; 2026 Anna Clerk Foundation. This is a fictional philanthropy concept.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    </div>

    <!-- Back to top -->
    <button class="ac-back-to-top" aria-label="Back to top">↑</button>

    <script src="{ROOT_PATH}assets/js/jquery.min.js"></script>
    <script src="{ROOT_PATH}assets/js/bootstrap.bundle.min.js"></script>
    <script src="{ROOT_PATH}assets/js/modernizr.custom.js"></script>
    <script src="{ROOT_PATH}assets/js/jquery.dlmenu.js"></script>
    <script src="{ROOT_PATH}assets/js/jquery-plugin-collection.js"></script>
    <script src="{ROOT_PATH}assets/js/script.js"></script>
    <script>
        // Back to top
        (function() {
            var btn = document.querySelector('.ac-back-to-top');
            if (!btn) return;
            window.addEventListener('scroll', function() {
                btn.classList.toggle('visible', window.scrollY > 400);
            });
            btn.addEventListener('click', function() {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        })();
    </script>
</body>"""

def process_file(filepath, is_event=False):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update CSS version
        content = re.sub(r'ac-overrides\.css\?v=\d+', 'ac-overrides.css?v=8', content)
        
        # Inject Skip link if it doesn't exist
        if '<a class="skip-link"' not in content:
            content = content.replace('<body>', '<body>\n    <a class="skip-link" href="#main">Skip to content</a>', 1)

        root_path = "../" if is_event else ""

        # Replace Header - matching <header id="header"> ... </header> block
        header_pattern = re.compile(r'<header id="header">.*?</header>', re.DOTALL | re.IGNORECASE)
        h_rep = header_replacement.replace("{ROOT_PATH}", root_path)
        if header_pattern.search(content):
            content = header_pattern.sub(h_rep, content)
        else:
            print(f"Header pattern not found in {filepath}")

        # Replace Footer - match various old newsletter/footer structures
        footer_patterns = [
            re.compile(r'<!-- Stories CTA.*?</body>', re.DOTALL | re.IGNORECASE),
            re.compile(r'<!-- Newsletter -->.*?</body>', re.DOTALL | re.IGNORECASE),
            re.compile(r'<footer class="wpo-site-footer">.*?</body>', re.DOTALL | re.IGNORECASE)
        ]
        
        f_rep = footer_replacement.replace("{ROOT_PATH}", root_path)
        
        footer_replaced = False
        for pattern in footer_patterns:
            if pattern.search(content):
                content = pattern.sub(f_rep, content)
                footer_replaced = True
                break
                
        if not footer_replaced:
            print(f"Footer pattern not found in {filepath}")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Successfully processed {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

directory = r"d:\Ke hoạch bạc tỷ\NGO"
for filename in os.listdir(directory):
    if filename.endswith(".html") and filename not in ['index.html', 'our-work.html']:
        process_file(os.path.join(directory, filename), is_event=False)

event_directory = os.path.join(directory, "events")
if os.path.exists(event_directory):
    for filename in os.listdir(event_directory):
        if filename.endswith(".html"):
            process_file(os.path.join(event_directory, filename), is_event=True)
