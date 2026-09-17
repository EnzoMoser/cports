pkgname = "caddy-oidc-devel"
pkgver = "0.4.3"
pkgrel = 0
pkgdesc = (
    "Caddy module that adds OIDC authentication and authorization termination"
)
license = "Apache-2.0"
url = "https://github.com/relvacode/caddy-oidc"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
]
source_paths = [
    "oidc",
]
sha256 = [
    "9c03680874137ac8785ffe46631123d830e1ef6be45a0e58412c092b1863df47",
]


def install(self):
    print(self.srcdir)
    self.install_files(
        "oidc",
        "usr/share/caddy-custom",
    )
