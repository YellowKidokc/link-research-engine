from dataclasses import dataclass


@dataclass
class DiscoveryRequest:
    case_title: str
    source_scope: str = "wikipedia_only"
    max_links: int = 25


def explain_discovery(request: DiscoveryRequest) -> str:
    return (
        f"Discover links for '{request.case_title}' "
        f"using scope={request.source_scope} max_links={request.max_links}."
    )
