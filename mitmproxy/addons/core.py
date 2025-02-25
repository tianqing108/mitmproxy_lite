import logging
import os
from collections.abc import Sequence

import mitmproxy.types
from mitmproxy import ctx
from mitmproxy import exceptions
from mitmproxy import flow
from mitmproxy import hooks
from mitmproxy import optmanager
from mitmproxy.log import ALERT
from mitmproxy.net.http import status_codes
from mitmproxy.utils import emoji

logger = logging.getLogger(__name__)

CONF_DIR = "~/.mitmproxy"
LISTEN_PORT = 8080


class Core:
    def configure(self, updated):
        opts = ctx.options
        if opts.add_upstream_certs_to_client_chain and not opts.upstream_cert:
            raise exceptions.OptionsError(
                "add_upstream_certs_to_client_chain requires the upstream_cert option to be enabled."
            )
        if "client_certs" in updated:
            if opts.client_certs:
                client_certs = os.path.expanduser(opts.client_certs)
                if not os.path.exists(client_certs):
                    raise exceptions.OptionsError(
                        f"Client certificate path does not exist: {opts.client_certs}"
                    )



