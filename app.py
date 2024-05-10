import streamlit as st

# Define a function for each page
def home():
    st.title('Overview')
    st.write('What is Diffusion?')
    st.header('Notes on online lectures')
    st.write(
        """
        What if, given a set of images, we could create--from seemingly thin air--an image that looks like it should belong exactly in that set?
        
        In mathematical language, this question is asking if we can efficiently learn to draw a sample from a given distribution of images.
        
        Sampling from some crazy distribution over images, you say? But don't we know how to sample from any sort of crazy distribution? Use Markov Chain Monte Carlo (MCMC) [separate blog post coming soon].
        
        Constructing an MCMC transition matrix for the space of images, however, is an extreme computational feat. How do you think about structuring the graph that you will randomly walk along? If each node is an image with a slightly different set of pixel values, that is an extremely dense graph.
        
        Instead, perhaps we can sample from a well-known distribution (like a normal distribution), and somehow construct a function that maps the well-known distribution into the distribution we actually care about.
        
        This is what diffusion models do.
        
        While we're still talking at the high level, here, it's worth noting that sampling from *any* distribution is powerful--it means we can also sample from conditional distributions. For example, we can sample from the distribution of images that are most probable given the statement "I love golden retrievers". We can condition on sentiments and ideas expressed in different modalities.
        """
    )
    st.write(
    """Compression is intelligence. Previous work on variational autoencoders reveals we can store compressed representations of data in a latent space.
    See my post on how variational autoencoders work here: [LINK]. So what if we perform diffusion not in pixel space but in latent space?
    """)
    st.header('Questions Confusing Chloe')
    st.write('How do you define MCMC over graphs in which neighbors vary with continuous values? i.e. in which neighbors are images with pixel values that differ by an differentiably small amount?')
    st.write('What does it really mean to align two modalities in latent space? like text and images? what does it mean to relate images with certain meaning to text with certain meaning?')

def browse_examples():
    st.title('Browse Examples')
    st.write('This is the Browse Examples Page.')

def ov_and_qk_circuits():
    st.title('OV and QK Circuits')
    st.write('This is the OV and QK Circuits Page.')

def copy_suppression_preserving_ablation():
    st.title('Copy Suppression-Preserving Ablation')
    st.write('This is the Copy Suppression-Preserving Ablation Page.')

def anti_induction_vs_copy_suppression():
    st.title('Anti Induction vs Copy Suppression')
    st.write('This is the Anti Induction vs Copy Suppression Page.')

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Tutorial Sections:', ['Home', 'Browse Examples', 'OV and QK circuits', 'Copy Suppression-Preserving Ablation', 'Anti Induction vs Copy Suppression'])

# Display the selected page
if page == 'Home':
    home()
elif page == 'Browse Examples':
    browse_examples()
elif page == 'OV and QK circuits':
    ov_and_qk_circuits()
elif page == 'Copy Suppression-Preserving Ablation':
    copy_suppression_preserving_ablation()
elif page == 'Anti Induction vs Copy Suppression':
    anti_induction_vs_copy_suppression()
