(function () {
    const LANG_KEY = "itSupportCvLang";
    const toggleBtn = document.getElementById("langToggle");

    function applyLanguage(lang) {
        const textNodes = document.querySelectorAll("[data-en][data-el]");
        const isGreek = lang === "el";

        textNodes.forEach((node) => {
            node.textContent = isGreek ? node.getAttribute("data-el") : node.getAttribute("data-en");
        });

        document.documentElement.lang = isGreek ? "el" : "en";
        if (toggleBtn) {
            toggleBtn.textContent = isGreek ? "English" : "Ελληνικά";
            toggleBtn.setAttribute("aria-label", isGreek ? "Switch language to English" : "Αλλαγή γλώσσας σε Ελληνικά");
        }

        window.localStorage.setItem(LANG_KEY, lang);
    }

    function getInitialLanguage() {
        const saved = window.localStorage.getItem(LANG_KEY);
        if (saved === "el" || saved === "en") {
            return saved;
        }

        // Default to Greek as requested.
        return "el";
    }

    const initialLang = getInitialLanguage();
    applyLanguage(initialLang);

    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            const nextLang = document.documentElement.lang === "el" ? "en" : "el";
            applyLanguage(nextLang);
        });
    }
})();
