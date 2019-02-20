from graphqlclient import GraphQLClient


class WeltGraphQLClient:

    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint
        self.api_key = api_key

    def retrieve_premium_content(self, page, page_size):
        query = '''
            { paginated_search( type:TextArticle excludeSections: "/testgpr/" flag: premium pageSize: %d page: %d) {
                results { 
                  id
                  webUrl
                  authors {
                    name
                  }
                  sectionData {
                    home {
                        URL
                    }
                  }
                  images(role:teaser) {
                    imageUrl_1x1: url(ratio: 1, size: 1200)
                    imageUrl_16x9: url(ratio: 1.777, size: 1200)
                  }
                  seoTitle
                  intro
                  readingTimeMinutes
                  premiumParagraph
                  publicationDate
                  headline
                  topic
                    }
                }
            }
            '''

        client = GraphQLClient(self.endpoint)
        client.inject_token(self.api_key, 'X-Api-Key')

        return client.execute(query % (page_size, page))
