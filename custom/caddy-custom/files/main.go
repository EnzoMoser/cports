// Taken from
// https://github.com/caddyserver/caddy/blob/master/cmd/caddy/main.go

package main

import (
    caddycmd "github.com/caddyserver/caddy/v2/cmd"

    // Standard Caddy Distribution
    _ "github.com/caddyserver/caddy/v2/modules/standard"

    // Forward auth
    _ "github.com/relvacode/caddy-oidc"
)

func main() {
    caddycmd.Main()
}
