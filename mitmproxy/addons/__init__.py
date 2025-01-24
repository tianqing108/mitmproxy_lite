from mitmproxy.addons import anticache
from mitmproxy.addons import anticomp
from mitmproxy.addons import block
from mitmproxy.addons import blocklist
from mitmproxy.addons import browser
from mitmproxy.addons import core
from mitmproxy.addons import disable_h2c
from mitmproxy.addons import dns_resolver
from mitmproxy.addons import next_layer
from mitmproxy.addons import proxyserver
from mitmproxy.addons import script
from mitmproxy.addons import stickyauth
from mitmproxy.addons import stickycookie
from mitmproxy.addons import strip_dns_https_records
from mitmproxy.addons import tlsconfig
from mitmproxy.addons import update_alt_svc
from mitmproxy.addons import upstream_auth


def default_addons():
    return [
        core.Core(),
        browser.Browser(),
        block.Block(),
        strip_dns_https_records.StripDnsHttpsRecords(),
        blocklist.BlockList(),
        anticache.AntiCache(),
        anticomp.AntiComp(),
        disable_h2c.DisableH2C(),
        proxyserver.Proxyserver(),
        dns_resolver.DnsResolver(),
        script.ScriptLoader(),
        next_layer.NextLayer(),
        stickyauth.StickyAuth(),
        stickycookie.StickyCookie(),
        tlsconfig.TlsConfig(),
        upstream_auth.UpstreamAuth(),
        update_alt_svc.UpdateAltSvc(),
    ]
