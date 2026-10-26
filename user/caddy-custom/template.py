pkgname = "caddy-custom"
pkgver = "2.11.7"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/caddyserver/caddy/v2.CustomVersion=v{pkgver}",
]
make_check_args = ["-p", "1", "./..."]
hostmakedepends = ["go"]
makedepends = [
    "caddy-oidc-devel",
    "dinit-chimera",
]
depends = ["shared-mime-info"]
renames = ["caddy"]
pkgdesc = "Extensible HTTP server with automatic HTTPS"
license = "Apache-2.0"
url = "https://caddyserver.com"
source = [
    f"https://github.com/caddyserver/caddy/archive/v{pkgver}.tar.gz",
]
source_paths = [
    "caddy",
]
sha256 = [
    "86e39de5fa0bc433a9cd574a00e7751059903401f3389c61f8937fd0ad0180f5",
]
# generates completions with host binary
options = ["!cross"]


def pre_prepare(self):
    self.cp(self.files_path / "main.go", ".")
    self.do("go", "mod", "init", "caddy")
    self.do(
        "go",
        "mod",
        "edit",
        "-replace",
        "github.com/caddyserver/caddy/v2=./caddy",
        "-replace",
        "github.com/relvacode/caddy-oidc=/usr/share/caddy-custom/oidc",
    )
    self.do("go", "mod", "tidy", allow_network=True)


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"caddy.{shell}", "w") as outf:
            self.do(
                "build/caddy",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "caddy")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"caddy.{shell}", shell, name="caddy")
